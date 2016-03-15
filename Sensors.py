from Plane import Plane
from math import *
import numpy as np

class Sensors(object):

    def __init__(self, name):
        self.name = name

    def __name__(self):
        return self.name


class EngineTempSensor(Sensors):

    def __init__(self, name):
        super(EngineTempSensor, self).__init__(name)
        self.magic = lambda x: math.log(x) + np.random.normal(0, 0.1)

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
        self.magic = np.random.normal(0, 0.1)

    def read(self,plane):
        al = plane.position()[2]
        return self.magic(al)



def ConstructSensorDict(listOfSensors):

    dict = {}
    for sensor in listOfSensors:
        dict[sensor.name()] = sensor
    return dict

