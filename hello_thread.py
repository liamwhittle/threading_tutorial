from slow import Slow
from fast import Fast
import time


class Master:
    def __init__(self):
        self.f = Fast()
        self.s = Slow()
        self.f.start()
        self.s.start()

    def print_update(self):
        while True:
            print(str(self.f.x) + " | " + str(self.s.x))
            time.sleep(.5)


m = Master()
m.print_update()