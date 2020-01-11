from GameWindow import GameWindow
from Multiplayer import Multiplayer
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QGroupBox, QGridLayout, QLabel
from PyQt5.QtCore import Qt


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
        self.widget2.clicked.connect(self.on_pushMultiPlayerButton_clicked)
        self.widget3.clicked.connect(self.on_pushExitButton_clicked)

        self.show()

    def on_pushExitButton_clicked(self):
        self.close()

    def on_pushSinglePlayerButton_clicked(self):
        self.dialog = GameWindow()
        self.dialog.show()
        #self.close()

    def on_pushMultiPlayerButton_clicked(self):
        self.dialog = Multiplayer()
        self.dialog.show()

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

