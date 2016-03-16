from Plane import Plane
from time import clock
from math import *
import numpy as np

class Sensors(object):

    def __init__(self, name):
        self.name = name

    def __name__(self):
        return self.name

    def getName(self):
        return self.name


class EngineTempSensor(Sensors):

    def __init__(self, name):
        super(EngineTempSensor, self).__init__(name)
        self.magic = lambda x: log(x) + np.random.normal(0, 0.1)

    def read(self, plane):
        vel = plane.velocity()
        return self.magic(vel)


class EngineFuelSensor(Sensors):

    def __init__(self, name):
        super(EngineFuelSensor,self).__init__(name)
        self.magic = lambda x: x**2 + np.random.normal(0, 0.1)

    def read(self, plane):
        vel = plane.velocity()
        return self.magic(vel)


class AltitudeSensor(Sensors):

    def __init__(self, name):
        super(AltitudeSensor,self).__init__(name)
        self.magic = lambda x: x + np.random.normal(0, 0.1)

    def read(self,plane):
        al = plane.position()[2]
        return self.magic(al)


class GPSSensor(Sensors):
    def __init__(self,name):
        super(GPSSensor,self).__init__(name)

    def read(self,plane):
        cord = {"X": str(plane.position()[0]), "Y": str(plane.position()[1])}
        return cord


class TimeSensor(Sensors):
    def __init__(self,name):
        super(TimeSensor,self).__init__(name)
        self.magic = lambda x: x + np.random.normal(0, 0.0001)

    def read(self,plane):
        t = clock()
        return self.magic(t)

class PressureSensor(Sensors):
    def __init__(self,name):
        super(PressureSensor,self).__init__(name)
        self.magic = lambda x: 1013 + exp(-x) + np.random.normal(0, 0.01)

    def read(self,plane):
        h = plane.position()[2]
        return self.magic(h)


def ConstructSensorDict(listOfSensors):

    dict = {}
    for sensor in listOfSensors:
        dict[sensor.getName()] = sensor
    return dict
