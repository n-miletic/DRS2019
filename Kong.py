from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsPixmapItem
class Kong():
    def __init__(self, a, b, red, green, blue, size, direction):
        self.i = a
        self.j = b
        #self.type = QGraphicsEllipseItem(self.i*size, self.j*size, size, size)
        #self.type.setBrush(QColor(red, green, blue))
        self.type = QGraphicsPixmapItem(QPixmap('./GResource/kong.gif'))
        self.type.setX(self.i * size)
        self.type.setY(self.j * size)
        self.direction = direction
