from datetime import timedelta
from PyQt5.QtCore import QTime, Qt, QTimer

class GameTime():
    def __init__(self):
        self.time = QTime()
        self.time.start()
        self.cur_time = ""

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.update_elapsed_time(self))
        self.timer.start(500)


    def update_elapsed_time(self):
        self.cur_time = timedelta(seconds=self.time.elapsed())










