from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsPixmapItem


class Player():
    def __init__(self, a, b, resource, size):
        self.i = a
        self.j = b
        self.maxJ = 19
        self.score = 0
        self.lives = 3
        self.res = resource
        # self.type = QGraphicsEllipseItem(self.i*size, self.j*size, size, size)
        # self.type.setBrush(QColor(red, green, blue))
        self.type = QGraphicsPixmapItem(QPixmap(self.res))
        self.type.setX(self.i * size)
        self.type.setY(self.j * size)
        self.isShielded = False
