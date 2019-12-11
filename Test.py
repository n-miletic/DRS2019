import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QGroupBox, QVBoxLayout, QLabel, \
    QDesktopWidget, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QMainWindow, QGraphicsEllipseItem

from PyQt5.QtCore import Qt, QRectF


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        # enables key event handling
        self.setFocusPolicy(Qt.StrongFocus)
        self.keys_pressed = set()

        self.size = 32
        self.setWindowTitle('Donkey Kong')
        self.setGeometry(300, 150, 10*self.size + 5, 20*self.size + 5)
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


class MainMenu(QWidget):

    def __init__(self):
        super().__init__()

        self.size = 64
        self.setWindowTitle('Golden Banana')
        self.setGeometry(300, 150, 15 * self.size, 11 * self.size)
        self.center()

        # coloring
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        self.widget1 = QPushButton('Single Player')
        self.widget2 = QPushButton('Multiplayer')
        self.widget3 = QPushButton('Exit')
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.widget1.clicked.connect(self.on_pushSinglePlayerButton_clicked)


        self.widget3.clicked.connect(self.on_pushExitButton_clicked)

        self.show()

    def on_pushExitButton_clicked(self):
        self.close()

    def on_pushSinglePlayerButton_clicked(self):
        self.dialog = GameWindow()
        self.dialog.show()
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()

        self.widget1.setFixedSize(200, 30)
        self.widget2.setFixedSize(200, 30)
        self.widget3.setFixedSize(200, 30)

        layout.addWidget(self.widget1, 5, 0)
        layout.addWidget(self.widget2, 6, 0)
        layout.addWidget(self.widget3, 7, 0)
        layout.addWidget(QLabel(" "), 0, 1)
        #layout.addWidget(QLabel(" "), 4, 1)
        #layout.addWidget(QLabel(" "), 5, 1)
        layout.addWidget(QLabel(" "), 6, 1)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainMenu()
    sys.exit(app.exec_())
