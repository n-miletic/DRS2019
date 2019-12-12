from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QDesktopWidget, \
    QGraphicsRectItem
from PyQt5.QtCore import Qt, QRectF
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
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'l', 'e'],
                       ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'l', 'b']]
        # e - empty, b - beam, l - ladder

        self.drawScene()

        self.player = QGraphicsEllipseItem(9*self.size, 19*self.size, self.size, self.size)
        self.player.setBrush(Qt.green)
        self.player_i = 9
        self.player_j = 19
        self.scene.addItem(self.player)

        self.show()

    # - when key is pressed
    def keyPressEvent(self, event):
        # self.keys_pressed.add(event.key())
        key = event.key()

        if key == Qt.Key_A:
            if (self.player_i - 1) > -1:
                if self.design[self.player_j][self.player_i-1] == 'b' or self.design[self.player_j][self.player_i-1] == 'l':
                    self.player_i -= 1
                    self.player.setX(self.player.x()-32)

        if key == Qt.Key_D:
            if (self.player_i + 1) < 10:
                if self.design[self.player_j][self.player_i+1] == 'b' or self.design[self.player_j][self.player_i+1] == 'l':
                    self.player_i += 1
                    self.player.setX(self.player.x()+32)

        if key == Qt.Key_W:
            if (self.player_j - 1) > -1:
                if self.design[self.player_j - 1][self.player_i] == 'l':
                    self.player_j -= 1
                    self.player.setY(self.player.y()-32)

        if key == Qt.Key_S:
            if (self.player_j + 1) < 20:
                if self.design[self.player_j + 1][self.player_i] == 'l':
                    self.player_j += 1
                    self.player.setY(self.player.y() + 32)

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

