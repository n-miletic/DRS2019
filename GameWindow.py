from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QDesktopWidget, \
    QGraphicsRectItem
from PyQt5.QtCore import Qt, QRectF, QBasicTimer
from PyQt5.QtGui import QColor
from Player import Player
from Kong import Kong
from Timer import time


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        # enables key event handling
        self.setFocusPolicy(Qt.StrongFocus)
        self.keys_pressed = set()

        #basic time to be implemented later into a timer
        self.statusBar().showMessage('{}'.format(time.toString()))

        #window settings and basic properties
        self.size = 32
        self.setWindowTitle('Donkey Kong')
        self.setGeometry(300, 150, 10*self.size + 10, 20*self.size + 25)
        #self.isGameOver = False
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
        # e - empty, b - beam, l - ladder

        self.drawScene()

        #player initialization
        self.player = Player(9, 19, 86, 130, 3, self.size)
        self.scene.addItem(self.player.type)

        #Donkey Kong initialization
        self.kong = Kong(0, 7, 123, 63, 0, self.size, 1);
        self.scene.addItem(self.kong.type)

        # -timer that synchronizes collision events
        self.game_update_timer = QBasicTimer()
        self.game_update_timer.start(20, self)

        # -timer that dictates movement kong's movement
        self.game_timer = QBasicTimer()
        self.game_timer.start(200, self)
        self.game_timer_id = self.game_timer.timerId()
        # -timer that dictates the speed at which barrels are dropped
        self.barrel_spawn_timer = QBasicTimer()
        self.barrel_spawn_timer.start(500, self)
        self.barrel_sp_Id = self.barrel_spawn_timer.timerId()
        # -timer that dictates the speed at which barrels are falling
        self.barrel_speed = 250
        self.barrel_movement_timer = QBasicTimer()
        self.barrel_movement_timer.start(self.barrel_speed, self)
        self.barrel_m_Id = self.barrel_movement_timer.timerId()
        self.is_barrel_thrown = False
        # -temporary barrel object
        self.barrel = QGraphicsEllipseItem(0*self.size, 0*self.size, self.size, self.size)
        self.barrel.setBrush(QColor(255, 215, 0))
        self.barrel_i = 0
        self.barrel_j = 0

        self.show()

    # - timer event starting the loop
    def timerEvent(self, event):
        if self.barrel_i == self.player.i and self.barrel_j == self.player.j:
            self.player.type.setX(0)
            self.player.type.setY(0)
            self.player.i = 9
            self.player.j = 19

        if self.game_timer_id == event.timerId():
            if 10 > (self.kong.i + self.kong.direction) > -1:
                if self.design[self.kong.j][self.kong.i + self.kong.direction] == 'b' or self.design[self.kong.j][self.kong.i + self.kong.direction] == 'l':
                    self.kong.type.setX(self.kong.type.x() + (self.size * self.kong.direction))
                    self.kong.i += self.kong.direction
                else:
                    self.kong.direction = self.kong.direction*(-1)
            else:
                self.kong.direction = self.kong.direction * (-1)

        if self.barrel_sp_Id == event.timerId():
            if not self.is_barrel_thrown:
                self.is_barrel_thrown = True
                self.barrel.setX(self.kong.type.x())
                self.barrel.setY((self.kong.j+1)*32)
                self.barrel_i = self.kong.i
                self.barrel_j = self.kong.j + 1
                self.scene.addItem(self.barrel)

        if self.barrel_m_Id == event.timerId():
            if self.is_barrel_thrown:
                if self.barrel_j < 19:
                    self.barrel.setY(self.barrel.y()+32)
                    self.barrel_j += 1
                else:
                    # end of the board
                    self.scene.removeItem(self.barrel)
                    self.is_barrel_thrown = False



        # if self.is_game_over is False:
            # self.game_update()
    # def game_update(self):
        # self.kong.setX(self.kong.x()+32)

    # - when key is pressed
    def keyPressEvent(self, event):
        self.kong.type.x() + 32
        # self.keys_pressed.add(event.key())
        key = event.key()

        if key == Qt.Key_A:
            if (self.player.i - 1) > -1:
                if self.design[self.player.j][self.player.i-1] == 'b' or self.design[self.player.j][self.player.i-1] == 'l':
                    self.player.i -= 1
                    self.player.type.setX(self.player.type.x()-32)

        if key == Qt.Key_D:
            if (self.player.i + 1) < 10:
                if self.design[self.player.j][self.player.i+1] == 'b' or self.design[self.player.j][self.player.i+1] == 'l':
                    self.player.i += 1
                    self.player.type.setX(self.player.type.x()+32)

        if key == Qt.Key_W:
            if (self.player.j - 1) > -1:
                if self.design[self.player.j - 1][self.player.i] == 'l':
                    self.player.j -= 1
                    self.player.type.setY(self.player.type.y()-32)

        if key == Qt.Key_S:
            if (self.player.j + 1) < 20:
                if self.design[self.player.j + 1][self.player.i] == 'l':
                    self.player.j += 1
                    self.player.type.setY(self.player.type.y() + 32)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def drawScene(self):
        for i in range(20):
            for j in range(10):
                newRect = QGraphicsRectItem(QRectF(j*32, i*32, self.size, self.size))
                if self.design[i][j] == 'e':
                    newRect.setBrush(Qt.black)
                elif self.design[i][j] == 'b':
                    newRect.setBrush(Qt.red)
                elif self.design[i][j] == 'l':
                    newRect.setBrush(Qt.magenta)

                self.scene.addItem(newRect)

