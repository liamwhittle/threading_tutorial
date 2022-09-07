from threading import Thread
import time


class Slow(Thread):
    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = 2

    def show(self):
        print(f"{self.x} + {self.y}")

    def run(self):
        i = 0
        while True:
            i += 1
            if i > 10:
                i = 0
            self.x = i
            time.sleep(2)
