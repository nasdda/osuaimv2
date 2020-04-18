from pynput.mouse import Controller
from time import sleep


class Hack:
    def __init__(self, filename):
        self.count = 0
        self.spos = [318, 151]
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
        self.timings = [[round((x*1.7)), round((y*1.6)), round(t / 1002, 5)] for x, y, t in self.timings]

        prev = self.timings[0]
        print(prev)
        print()

        for i in range(1,len(self.timings)):
            temp = self.timings[i][:] # remember current
            self.timings[i][0] -= prev[0]
            self.timings[i][1] -= prev[1]
            prev = temp

        for x in self.timings:
            print(x)
        self.size = len(self.timings)
        self.mouse = Controller()

##################################
    def start(self):
        x,y = self.mouse.position
        self.mouse.move(self.spos[0] - x, self.spos[1] - y)
        self.mouse.move(self.timings[0][0], self.timings[0][1])
        for x,y,d in self.timings[1:]:
            sleep(d)
            self.mouse.move(x,y)



    def next(self):
        x,y,d = self.timings[self.count]
        self.move(x,y)
        self.count += 1
