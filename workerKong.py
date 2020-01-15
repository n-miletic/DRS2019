from worker import Worker
import multiprocessing as mp

class WorkerKong(Worker):
    def __init__(self, pipe: mp.Pipe):
        super().__init__()
        self.pipe = pipe

    def work(self):
        self.pipe.send('go')
        while True:
            val = self.pipe.recv()
            if val == 'end':
                # notify all
                # in this case: kill the thread
                self.finished.emit()
                break
            if val == 'start':
                self.update.emit()

    def finishWork(self):
        self.pipe.send('end')
