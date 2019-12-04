import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.size = 64
        self.setWindowTitle('Test')
        self.setGeometry(300, 150, 15 * self.size, 11 * self.size)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())
