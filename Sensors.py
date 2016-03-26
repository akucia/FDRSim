from Plane import Plane
from time import clock
from math import *
import numpy as np


class Sensors(object):

    def __init__(self, name, plane):
        self.name = name
        self.plane = plane

    def getName(self):
        return self.name


class EngineTempSensor(Sensors):

    def __init__(self, name, plane):
        super(EngineTempSensor, self).__init__(name, plane)
        self.magic = lambda x: round(log(x) + np.random.normal(0, 0.1),2)

    def read(self):
        vel = self.plane.getVelocity()
        return self.magic(vel)


class EngineFuelSensor(Sensors):

    def __init__(self, name, plane):
        super(EngineFuelSensor, self).__init__(name, plane)
        self.magic = lambda x: round(x**2 + np.random.normal(0, 0.1),2)

    def read(self):
        vel = self.plane.getVelocity()
        return self.magic(vel)


class AltitudeSensor(Sensors):

    def __init__(self, name, plane):
        super(AltitudeSensor, self).__init__(name, plane)
        self.magic = lambda x: round(x + np.random.normal(0, 0.1),2)

    def read(self):
        al = self.plane.getPosition()[2]
        return self.magic(al)

""" not working...
class GPSSensor(Sensors):
    def __init__(self, name):
        super(GPSSensor, self).__init__(name, plane)

    def read(self):
        cord = {"X": str(self.plane.position()[0]), "Y": str(self.plane.position()[1])}
        return cord
"""

class TimeSensor(Sensors):
    def __init__(self, name, plane):
        super(TimeSensor, self).__init__(name, plane)
        self.magic = lambda x: round(x,2)

    def read(self):
        return self.magic(self.plane.getTime())


class PressureSensor(Sensors):
    def __init__(self, name, plane):
        super(PressureSensor,self).__init__(name, plane)
        self.magic = lambda x: round(1013 + exp(-x) + np.random.normal(0, 0.1),2)

    def read(self):
        h = self.plane.getPosition()[2]
        return self.magic(h)


class WheelsONOFF(Sensors):
    def __init__(self, name, plane):
        super(WheelsONOFF, self).__init__(name, plane)

    def read(self):
        if self.plane.position()[2] > 1000:
            return True
        else:
            return False


class SensorFactory(object):
    @staticmethod
    def createSensor(sensorType, numberStr, plane):
        if sensorType == 'EngineTempSensor':
            return EngineTempSensor(sensorType + numberStr,plane)
        elif sensorType == 'EngineFuelSensor':
            return EngineFuelSensor(sensorType + numberStr,plane)
        elif sensorType == 'AltitudeSensor':
            return AltitudeSensor(sensorType + numberStr,plane)
        elif sensorType == 'TimeSensor':
            return TimeSensor(sensorType + numberStr, plane)
        elif sensorType == 'PressureSensor':
            return PressureSensor(sensorType + numberStr,plane)
        elif sensorType == 'WheelsONOFF':
            return WheelsONOFF(sensorType + numberStr,plane)
    @staticmethod
    def createSensorList(sensorsDict, plane):
        list = []
        for sensorName in sensorsDict.keys():
            for i in range(sensorsDict[sensorName]):
                list.append(SensorFactory.createSensor(sensorName,'#'+str(i+1),plane))
        return list


def ConstructSensorDict(listOfSensors):

    dict = {}
    for sensor in listOfSensors:
        dict[sensor.getName()] = sensor
    return dict
