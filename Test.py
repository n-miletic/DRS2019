import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QGroupBox, QVBoxLayout, QLabel


class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.size = 64
        self.setWindowTitle('Test')
        self.setGeometry(300, 150, 15 * self.size, 11 * self.size)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        #layout.setColumnStretch(1, 4)
        #layout.setColumnStretch(2, 4)

        widget1 = QPushButton('Single Player')
        widget1.setFixedSize(200,30)
        widget2 = QPushButton('Multiplayer')
        widget2.setFixedSize(200,30)
        widget3 = QPushButton('Exit')
        widget3.setFixedSize(200,30)

        layout.addWidget(widget1, 1, 1)
        layout.addWidget(widget2, 2, 1)
        layout.addWidget(widget3, 3, 1)
        layout.addWidget(QLabel(" "), 0, 1)
        layout.addWidget(QLabel(" "), 4, 1)
        layout.addWidget(QLabel(" "), 5, 1)
        layout.addWidget(QLabel(" "), 6, 1)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())
