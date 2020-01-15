from multiprocessing import Process, Pipe

import time


class ProcessKong(Process):

    def __init__(self, pipe: Pipe):
        super().__init__(target=self.doProcess, args=[pipe])

    def doProcess(self, pipe: Pipe):
        pipe.recv()
        pipe.send('start')
        pipe.recv()
        pipe.send('end')
