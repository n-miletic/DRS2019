from datetime import timedelta

from PyQt5.QtCore import QTime, Qt, QTimer


class Timer():
    def __init__(self):
        self.time = QTime(self)
        self.time.start(self)
        self.cur_time = ""

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: update_elapsed_time())
        self.timer.start(self, 500)

        def update_elapsed_time():
            cur_time = timedelta(seconds=self.time.elapsed())










