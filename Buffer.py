from Sensors import *
from copy import deepcopy
from time import clock, sleep
class Buffer(object):


    def __init__(self, freq):
        self.freq = freq
        self.allReadings = []
        self.time = clock()
        self.period = float(1)/float(self.freq)

    def readData(self, sensorList):

        while clock() - self.time < self.period:
            pass

        self.time = clock()

        buffer = []
        for sensor in sensorList:
            buffer.append(sensor.read())
        self.allReadings.append(buffer)

    def returnDataCopy(self):
        return deepcopy(self.allReadings)

    def printData(self):
        for line in self.allReadings:
            for number in line:
                print repr(number).rjust(10),
                print('\t'),
            print