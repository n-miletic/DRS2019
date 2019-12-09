import sys

from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QGroupBox, QVBoxLayout, QLabel, \
    QDesktopWidget, QGraphicsGridLayout, QGraphicsItem, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QMainWindow
from PyQt5.QtCore import Qt, QRectF


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        self.size = 32
        self.setWindowTitle('Donkey Kong')
        self.setGeometry(300, 150, 10*self.size + 5, 20*self.size + 5)

        self.center()
        self.scene = QGraphicsScene(self)
        view = QGraphicsView(self.scene)
        self.setCentralWidget(view)

        self.drawScene()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def drawScene(self):
        for i in range(10):
            for j in range(20):
                newRect = QGraphicsRectItem(QRectF(i*32, j*32, self.size, self.size))
                if j%2 == 0:
                    newRect.setBrush(Qt.red)
                else:
                    newRect.setBrush(Qt.black)

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
