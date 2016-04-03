from Sensors import Sensors, SensorFactory
from copy import deepcopy
from time import clock, sleep

class Buffer(object):
# TODO tidy up this class

    def __init__(self, freq, sensorList):
        self.sensorList = sensorList
        self.freq = freq
        self.allReadings = []
        self.allReadingsHorizontal = []
        self.time = clock()
        self.period = float(1)/float(self.freq)
        for i in range(len(sensorList)):
            list = []
            self.allReadingsHorizontal.append(list)

    def readData(self):

        while clock() - self.time < self.period:
            pass

        self.time = clock()

        buffer = []
        i = 0
        for sensor in self.sensorList:
            buffer.append(sensor.read())
            self.allReadingsHorizontal[i].append(sensor.read())
            i += 1
        self.allReadings.append(buffer)


    def returnDataCopy(self):
        return deepcopy(self.allReadings)

    def returnDataHorizontal(self):
        return self.allReadingsHorizontal

    def printData(self):
        for line in self.allReadings:
            for number in line:
                print (number, '\t',end=" ")
            print()