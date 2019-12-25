from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsEllipseItem
class Barrel():
    def __init__(self, a, b, red, green, blue, size, speed):
        self.i = a
        self.j = b
        self.type = QGraphicsEllipseItem(self.i*size, self.j*size, size, size)
        self.type.setBrush(QColor(red, green, blue))
        self.spawnTimer = QBasicTimer()
        self.speed = speed
        self.movementTimer = QBasicTimer()
        self.isBarrelThrown = False
        self.spawnID = self.spawnTimer.timerId()
        self.mvmID = self.movementTimer.timerId()
