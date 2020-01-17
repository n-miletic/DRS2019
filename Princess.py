from PyQt5.QtGui import QColor, QPixmap, QMovie
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsPixmapItem, QLabel


class Princess():
    def __init__(self, red, green, blue, size):
        self.i = 3
        self.j = 2
        #self.type = QGraphicsEllipseItem(self.i * size, self.j * size, size, size)
        #self.type.setBrush(QColor(red, green, blue))

        self.type = QGraphicsPixmapItem(QPixmap('./GResource/princess.gif'))
        self.type.setX(self.i * size)
        self.type.setY(self.j * size)

        #self.type = QLabel('')
        #movie = QMovie('./GResource/princess.gif')
        #self.type.setMovie(movie)
        #movie.start()
        #self.type.move(self.i * size, self.j * size)



