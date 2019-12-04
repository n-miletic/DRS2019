import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QGroupBox, QVBoxLayout, QLabel,\
    QDesktopWidget
from PyQt5.QtCore import Qt


class GameWindow(QWidget):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        self.size = 64
        self.setWindowTitle('Donkey Kong')
        self.setGeometry(300, 150, 5*self.size, 15*self.size)
        self.center()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
        self.dialogs = list()
        self.show()

    def on_pushSinglePlayerButton_clicked(self):
        dialog = GameWindow(self)
        self.dialogs.append(dialog)
        self.dialog.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()

        self.widget1.setFixedSize(200,30)
        self.widget2.setFixedSize(200,30)
        self.widget3.setFixedSize(200,30)

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
