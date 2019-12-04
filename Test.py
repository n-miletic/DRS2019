import sys
import math

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QGroupBox, QVBoxLayout, QLabel,\
    QDesktopWidget
from PyQt5.QtCore import Qt


class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.size = 64
        self.setWindowTitle('Test')
        self.setGeometry(300, 150, 15 * self.size, 11 * self.size)
        self.center()
        # coloring
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()

        widget1 = QPushButton('Single Player')
        widget1.setFixedSize(200,30)
        widget2 = QPushButton('Multiplayer')
        widget2.setFixedSize(200,30)
        widget3 = QPushButton('Exit')
        widget3.setFixedSize(200,30)

        layout.addWidget(widget1, 5, 0)
        layout.addWidget(widget2, 6, 0)
        layout.addWidget(widget3, 7, 0)
        layout.addWidget(QLabel(" "), 0, 1)
        layout.addWidget(QLabel(" "), 4, 1)
        layout.addWidget(QLabel(" "), 5, 1)
        layout.addWidget(QLabel(" "), 6, 1)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())
