from pyautogui import moveTo
from time import sleep


class Hack:
    def __init__(self, filename):
        self.count = 0
        self.spos = [398, 187]
        self.scaleX = 2.2
        self.scaleY = 1.9
        self.file = open(filename, 'r', encoding='utf8')
        curr = self.file.readline()
        while not '[HitObjects]' in curr:  # ignores data before hitobjects
            curr = self.file.readline()
        self.timings = self.file.readlines()
        self.timings = [x.split(',')[:3] for x in self.timings]
        self.timings = [[int(x) for x in y] for y in self.timings]
        curr = self.timings[0][-1]
        self.timings[0][-1] = 0

        for i in range(1, len(self.timings)):
            temp = self.timings[i][-1]
            self.timings[i][-1] -= curr
            curr = temp
        self.timings = [[x, y, round(t / 1000, 5)] for x, y, t in self.timings]
        for x in self.timings:
            print(x)

        self.size = len(self.timings)

    def move(self, x, y, d=0):
        moveTo(self.spos[0] + (x * self.scaleX), self.spos[1] + (y * self.scaleY), duration=d)

    def start(self):
        for data in self.timings:
            self.move(data[0], data[1])
            sleep(data[-1])

    def next(self):
        if self.count == self.size:
            return
        self.move(self.timings[self.count][0], self.timings[self.count][1])
        self.count += 1
