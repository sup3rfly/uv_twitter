import time

class tmr:
    #counter = 60
    def __init__(self, t=10):
        self.counter = 6

    def timer(self):
        if self.counter != 0:
            time.sleep(10)
            self.counter -= 1
            return self.counter
        else:
            return False