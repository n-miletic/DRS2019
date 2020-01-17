from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QDesktopWidget, \
    QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from threading import Thread
from PyQt5.QtCore import Qt, QRectF, QBasicTimer, pyqtSlot
from PyQt5.QtGui import QColor, QPixmap
from Player import Player
from Kong import Kong
from Timer import Timer
from Barrel import Barrel
from PowerUp import PowerUp
from Princess import Princess
from workerKong import WorkerKong
import random
import time
import multiprocessing as mp


class GameWindow(QMainWindow):
    powerUpTable = (
        (3, 15), (9, 11), (0, 19)
    )

    def __init__(self, pipe: mp.Pipe, parent=None):
        super(GameWindow, self).__init__(parent)

        # enables key event handling
        self.setFocusPolicy(Qt.StrongFocus)
        self.keys_pressed = set()

        self.worker = WorkerKong(pipe)

        # basic time to be implemented later into a timer
        # -self.statusBar().showMessage('{}'.format(time.toString()))
        self.statusBar().showMessage('{}'.format("0:00:00"))
        # self.statusBar().showMessage('{}'.format(""))

        # window settings and basic properties
        self.size = 32
        self.setWindowTitle('Donkey Kong')
        self.setGeometry(300, 150, 10*self.size + 10, 20*self.size + 25)
        # self.isGameOver = False
        self.center()
        self.scene = QGraphicsScene(self)
        view = QGraphicsView(self.scene)
        self.setCentralWidget(view)

        self.design = [['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'e', 'b', 'b', 'l', 'b', 'b', 'e', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'l', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'l', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'l', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'l', 'e', 'e', 'e', 'e'],
                       ['b', 'b', 'l', 'b', 'b', 'l', 'b', 'b', 'e', 'e'],
                       ['e', 'e', 'l', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'l', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'l', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
                       ['e', 'e', 'l', 'b', 'b', 'b', 'b', 'b', 'l', 'b'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'b', 'b', 'b', 'b', 'b', 'l', 'b'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'l', 'b']]
        # e - empty, b - beam, l - ladder, p - power up

        self.worker.update.connect(self.listen)
        self.worker.start()

        # powerUp initialization
        (a, b) = self.setRandomPosition()
        self.powerUp = PowerUp(a, b, 0, 0, 255, self.size)

        # player initialization
        self.player = Player(9, 19, 86, 130, 3, self.size)

        # princess initialization
        self.princess = Princess(255, 192, 203, self.size)

        # Donkey Kong initialization
        self.kong = Kong(0, 7, 123, 63, 0, self.size, 1)

        # -timer that synchronizes collision events
        self.game_update_timer = QBasicTimer()
        self.game_update_timer.start(20, self)

        # -timer that dictates movement kong's movement
        self.game_timer = QBasicTimer()
        self.game_timer.start(200, self)
        self.game_timer_id = self.game_timer.timerId()

        # -temporary barrel object
        self.barrel = Barrel(0, 0, 255, 215, 0, self.size, 250)
        # -timer that dictates the speed at which barrels are dropped
        self.barrel.spawnTimer.start(500, self)
        self.barrel.spawnID = self.barrel.spawnTimer.timerId()
        # -timer that dictates the speed at which barrels are falling
        self.barrel.movementTimer.start(self.barrel.speed, self)
        self.barrel.mvmID = self.barrel.movementTimer.timerId()

        # -game time passed
        self.elapsed_timer = Timer()

        self.elapsed_timer_thread = Thread(target=self.elapsed_time_scheduler)
        self.elapsed_timer_thread.start()

        self.show()

    def setRandomPosition(self):
        return GameWindow.powerUpTable[random.randint(0, 2)]

    # - timer event starting the loop
    def timerEvent(self, event):
        if self.barrel.i == self.player.i and self.barrel.j == self.player.j and self.barrel.isBarrelThrown:
            self.barrel.isBarrelThrown = False
            if self.player.isShielded:
                self.player.isShielded = False
                self.player.type.setBrush(QColor(86, 130, 3))
            else:
                self.player.lives -= 1
                if self.player.lives == 0:
                    self.player.type.setX(0)
                    self.player.type.setY(0)
                    self.player.i = -2
                    self.player.j = -2
                    self.scene.removeItem(self.player.type)
                    self.game_over_event()
                else:
                    self.player.i = 9
                    self.player.type.setX(0)
                    self.player.j = 19
                    self.player.type.setY(0)
            self.scene.removeItem(self.barrel.type)

        if self.player.i == self.kong.i and self.player.j == self.kong.j:
            self.player.lives -= 1
            if self.player.lives == 0:
                self.player.type.setX(0)
                self.player.type.setY(0)
                self.player.i = -2
                self.player.j = -2
                self.scene.removeItem(self.player.type)
                self.game_over_event()
            else:
                self.player.i = 9
                self.player.type.setX(0)
                self.player.j = 19
                self.player.type.setY(0)

        if self.game_timer_id == event.timerId():
            if 10 > (self.kong.i + self.kong.direction) > -1:
                if self.design[self.kong.j][self.kong.i + self.kong.direction] == 'b' or self.design[self.kong.j][self.kong.i + self.kong.direction] == 'l':
                    self.kong.type.setX(self.kong.type.x() + (self.size * self.kong.direction))
                    self.kong.i += self.kong.direction
                else:
                    self.kong.direction = self.kong.direction*(-1)
            else:
                self.kong.direction = self.kong.direction * (-1)

        if self.barrel.spawnID == event.timerId():
            if not self.barrel.isBarrelThrown:
                self.barrel.isBarrelThrown = True
                self.barrel.type.setX(self.kong.type.x())
                self.barrel.type.setY((self.kong.j+1)*32)
                self.barrel.i = self.kong.i
                self.barrel.j = self.kong.j + 1
                self.scene.addItem(self.barrel.type)

        if self.barrel.mvmID == event.timerId():
            if self.barrel.isBarrelThrown:
                if self.barrel.j < 19:
                    self.barrel.type.setY(self.barrel.type.y()+32)
                    self.barrel.j += 1
                else:
                    # end of the board
                    self.scene.removeItem(self.barrel.type)
                    self.barrel.isBarrelThrown = False

    def levelUp(self):
        self.kong.i = 0
        self.kong.type.setX(0)
        self.kong.j = 7
        self.kong.type.setY(0)
        self.player.i = 9
        self.player.type.setX(0)
        self.player.j = 19
        self.player.type.setY(0)
        self.player.maxJ = 19
        if self.barrel.speed > 25:
            self.barrel.speed -= 25
            self.barrel.movementTimer.stop()
            self.barrel.movementTimer.start(self.barrel.speed, self)
        self.barrel.isBarrelThrown = False
        (a, b) = self.setRandomPosition()
        self.scene.removeItem(self.powerUp.type)
        self.powerUp.i = a
        self.powerUp.type.setX(0)
        self.powerUp.j = b
        self.powerUp.type.setY(0)
        self.scene.addItem(self.powerUp.type)

    def game_over_event(self):
        points = 'Elapsed time:{}  || P1: Score:{}'.format(
            self.elapsed_timer.cur_time.seconds, self.player.score)
        buttonReply = QMessageBox.question(self, 'Game over', 'Total ' + points, QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            self.elapsed_timer_thread.isAlive = False
            self.close()

    # - when key is pressed
    def keyPressEvent(self, event):
        self.kong.type.x() + 32
        # self.keys_pressed.add(event.key())
        key = event.key()

        if key == Qt.Key_A:
            if (self.player.i - 1) > -1:
                if self.design[self.player.j][self.player.i-1] == 'b' or self.design[self.player.j][self.player.i-1] == 'l':
                    if self.player.i == self.powerUp.i and self.player.j == self.powerUp.j:
                        self.player.isShielded = True
                        self.player.type.setBrush(QColor(0, 135, 189))
                        self.scene.removeItem(self.powerUp.type)
                    self.player.i -= 1
                    self.player.type.setX(self.player.type.x()-32)
                    if self.player.i == self.princess.i and self.player.j == self.princess.j:
                        self.levelUp()

        if key == Qt.Key_D:
            if (self.player.i + 1) < 10:
                if self.design[self.player.j][self.player.i+1] == 'b' or self.design[self.player.j][self.player.i+1] == 'l':
                    if self.player.i == self.powerUp.i and self.player.j == self.powerUp.j:
                        self.player.isShielded = True
                        self.player.type.setBrush(QColor(0, 135, 189))
                        self.scene.removeItem(self.powerUp.type)
                    self.player.i += 1
                    self.player.type.setX(self.player.type.x()+32)

        if key == Qt.Key_W:
            if (self.player.j - 1) > -1:
                if self.design[self.player.j - 1][self.player.i] == 'l':
                    if self.player.i == self.powerUp.i and self.player.j == self.powerUp.j:
                        self.player.isShielded = True
                        self.player.type.setBrush(QColor(0, 135, 189))
                        self.scene.removeItem(self.powerUp.type)
                    self.player.j -= 1
                    if self.player.maxJ > self.player.j:
                        self.player.maxJ = self.player.j
                        if self.player.maxJ == 2 or self.player.maxJ == 7 or self.player.maxJ == 11 or self.player.maxJ == 15 or self.player.maxJ == 19:
                            self.player.score += 1
                    self.player.type.setY(self.player.type.y()-32)

        if key == Qt.Key_S:
            if (self.player.j + 1) < 20:
                if self.design[self.player.j + 1][self.player.i] == 'l':
                    if self.player.i == self.powerUp.i and self.player.j == self.powerUp.j:
                        self.player.isShielded = True
                        self.player.type.setBrush(QColor(0, 135, 189))
                        self.scene.removeItem(self.powerUp.type)
                    self.player.j += 1
                    self.player.type.setY(self.player.type.y() + 32)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def elapsed_time_scheduler(self):
        while True:
            self.elapsed_timer.update_elapsed_time()
            self.statusBar().showMessage('Elapsed time:{}  || P1: Lives:{} Score:{}'.format(self.elapsed_timer.cur_time.seconds, self.player.lives, self.player.score))
            time.sleep(0.5)

    @pyqtSlot()
    def listen(self):
        for i in range(20):
            for j in range(10):
                newRect = QGraphicsRectItem(QRectF(j*32, i*32, self.size, self.size))
                newPixmap = QGraphicsPixmapItem(QPixmap('./GResource/Beam.png'))
                newPixmap.setX(j * 32)
                newPixmap.setY(i * 32)
                if self.design[i][j] == 'e':
                    newRect.setBrush(Qt.black)
                elif self.design[i][j] == 'b':
                    #newRect.setBrush(Qt.red)
                    newRect = newPixmap
                    self.scene.addItem(newPixmap)
                elif self.design[i][j] == 'l':
                    #newRect.setBrush(Qt.magenta)
                    newPixmap = QGraphicsPixmapItem(QPixmap('./GResource/Ladder.png'))
                    newPixmap.setX(j * 32)
                    newPixmap.setY(i * 32)
                    newRect = newPixmap

                self.scene.addItem(newRect)

        self.addStuff()

    def addStuff(self):
        self.scene.addItem(self.powerUp.type)
        self.scene.addItem(self.player.type)
        self.scene.addItem(self.princess.type)
        self.scene.addItem(self.kong.type)
        self.worker.finishWork()

