from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QBasicTimer, QTimer

import time
import threading
from threading import Timer


class TimeTriggers(QObject):

    drop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.is_done = False

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

        self.game_update_timer = QTimer()
        self.game_update_timer.timeout.connect(self.timerEvent)
        self.game_update_timer.moveToThread(self.thread)
        self.game_update_timer.start(500)
        self.thread.start()

    def start(self):
        self.thread.start()

    def timerEvent(self, event):
        self.drop_barrel()

    @pyqtSlot()
    def drop_barrel(self):
        self.drop_signal.emit()

    def __work__(self):
        while not self.is_done:
            time.sleep(0.03)
