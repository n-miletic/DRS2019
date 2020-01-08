from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsEllipseItem

class Princess():
    def __init__(self, red, green, blue, size):
        self.i = 3
        self.j = 2
        self.type = QGraphicsEllipseItem(self.i * size, self.j * size, size, size)
        self.type.setBrush(QColor(red, green, blue))