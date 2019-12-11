import sys
from MainWindow import MainMenu

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainMenu()
    sys.exit(app.exec_())
