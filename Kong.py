from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsEllipseItem
class Kong():
    def __init__(self, a, b, red, green, blue, size, direction):
        self.i = a
        self.j = b
        self.type = QGraphicsEllipseItem(self.i*size, self.j*size, size, size)
        self.type.setBrush(QColor(red, green, blue))
        self.direction = direction
