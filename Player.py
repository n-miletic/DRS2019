from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsEllipseItem
class Player():
    def __init__(self, a, b, red, green, blue, size):
        self.i = a
        self.j = b
        self.type = QGraphicsEllipseItem(self.i*size, self.j*size, size, size)
        self.setBrush(QColor(red,green,blue))