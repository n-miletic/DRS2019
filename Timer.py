from datetime import timedelta

from PyQt5.QtCore import QTime, Qt, QTimer

time = QTime()
time.start()
cur_time = ""

timer = QTimer()
timer.timeout.connect(lambda: update_elapsed_time())
timer.start(500)


def update_elapsed_time():
    cur_time = timedelta(seconds=time.elapsed())










