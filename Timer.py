from datetime import timedelta
import datetime

from PyQt5.QtCore import QTime, Qt, QTimer, QDateTime


class Timer():
    def __init__(self):
        self.time = QTime()
        self.time.start()
        self.cur_time = timedelta(milliseconds=self.time.elapsed())
        # self.stop_time = self.time.
        # self.cur_time = self.stop_time - self.time

    def update_elapsed_time(self):
        self.cur_time = timedelta(milliseconds=self.time.elapsed())
        # self.cur_time = self.time.elapsed()
        # self.cur_time = self.stop_time - self.time










