from Sensors import Sensors, SensorFactory
from copy import deepcopy
from time import clock, sleep

class Buffer(object):
# TODO tidy up this class

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
                print (number, '\t',end=" ")
                #print repr(number).rjust(10), used to work in python 2.7
                #print(),
            print()