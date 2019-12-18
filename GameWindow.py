from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QDesktopWidget, \
    QGraphicsRectItem
from PyQt5.QtCore import Qt, QRectF, QBasicTimer
from PyQt5.QtGui import QColor
from Player import Player
from Timer import time


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        # enables key event handling
        self.setFocusPolicy(Qt.StrongFocus)
        self.keys_pressed = set()

        #basic time to be implemented later into a timer

        self.statusBar().showMessage('{}'.format(time.toString()))

        self.size = 32
        self.setWindowTitle('Donkey Kong')
        self.setGeometry(300, 150, 10*self.size + 10, 20*self.size + 25)
        self.is_game_over = False


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

        self.player = Player(9, 19, 86, 130, 3, self.size)
        self.scene.addItem(self.player.type)

        self.kong = QGraphicsEllipseItem(0*self.size, 7*self.size, self.size, self.size)
        self.kong.setBrush(QColor(123, 63, 0))
        self.kong_i = 0
        self.kong_j = 7
        self.kong_direction = 1
        self.scene.addItem(self.kong)

        self.game_timer = QBasicTimer()
        self.game_timer.start(200, self)
        self.game_timer_id = self.game_timer.timerId()

        self.show()

    # - timer event starting the loop
    def timerEvent(self, event):
        if self.game_timer_id == event.timerId():
            if 10 > (self.kong_i + self.kong_direction) > -1:
                if self.design[self.kong_j][self.kong_i + self.kong_direction] == 'b' or self.design[self.kong_j][self.kong_i + self.kong_direction] == 'l':
                    self.kong.setX(self.kong.x() + (self.size * self.kong_direction))
                    self.kong_i += self.kong_direction
                else:
                    self.kong_direction = self.kong_direction*(-1)
            else:
                self.kong_direction = self.kong_direction * (-1)

        # if self.is_game_over is False:
            # self.game_update()
    # def game_update(self):
        # self.kong.setX(self.kong.x()+32)

    # - when key is pressed
    def keyPressEvent(self, event):
        self.kong.x() + 32
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

