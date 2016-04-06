from math import *
import numpy as np


class Sensors(object):
    """
    abstract class of Sensors
    """
    # TODO tidy up
    def __init__(self, name, plane):
        """

        :param name: a string, name of the sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: none
        """
        self.name = name
        self.plane = plane

    def getName(self):
        """

        :return: name of the sensor
        """
        return self.name


class EngineTempSensor(Sensors):
    """
    simulation of sensor, inherits from Sensors class
    """
    def __init__(self, name, plane):
        """
        initialization
        :param name: a string, name of the sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: none
        """
        super(EngineTempSensor, self).__init__(name, plane)
        self.magic = lambda: round(400 + np.random.normal(0, 0.01), 2)

    def read(self):
        """

        :return: a float, reading from this sensor
        """
        return self.magic()


class EngineFuelSensor(Sensors):
    """
    simulation of sensor, inherits from Sensors class
    """
    def __init__(self, name, plane):
        """
        initialization
        :param name: a string, name of the sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: none
        """
        super(EngineFuelSensor, self).__init__(name, plane)
        self.magic = lambda x: round(x**2 + np.random.normal(0, 0.01), 2)

    def read(self):
        """

        :return: a float, reading from this sensor
        """
        vel = self.plane.getVelocity()
        return self.magic(vel)


class AltitudeSensor(Sensors):
    """
    simulation of sensor, inherits from Sensors class
    """
    def __init__(self, name, plane):
        """
        initialization
        :param name: a string, name of the sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: none
        """
        super(AltitudeSensor, self).__init__(name, plane)
        self.magic = lambda x: round(x + np.random.normal(0, 0.01),2)

    def read(self):
        """

        :return: a float, reading from this sensor
        """
        al = self.plane.getPosition()[2]
        return self.magic(al)


class TimeSensor(Sensors):
    """
    simulation of sensor, inherits from Sensors class
    """
    def __init__(self, name, plane):
        """
        initialization
        :param name: a string, name of the sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: none
        """
        super(TimeSensor, self).__init__(name, plane)
        self.magic = lambda x: round(x,2)

    def read(self):
        """

        :return: a float, reading from this sensor
        """
        return self.magic(self.plane.getTime())


class PressureSensor(Sensors):
    """
    simulation of sensor, inherits from Sensors class
    """
    def __init__(self, name, plane):
        """
        initialization
        :param name: a string, name of the sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: none
        """
        super(PressureSensor,self).__init__(name, plane)
        self.magic = lambda x: round(1013 + exp(-x) + np.random.normal(0, 0.01),2)

    def read(self):
        """

        :return: a float, reading from this sensor
        """
        h = self.plane.getPosition()[2]
        return self.magic(h)


class WheelsONOFF(Sensors):
    """
    ---not used in main program---
    simulation of sensor, inherits from Sensors class
    """
    def __init__(self, name, plane):
        """
        initialization
        :param name: a string, name of the sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: none
        """
        super(WheelsONOFF, self).__init__(name, plane)

    def read(self):
        """

        :return: a float, reading from this sensor
        """
        if self.plane.position()[2] > 1000:
            return True
        else:
            return False


class SensorFactory(object):
    """
    class for dynamic creation of Sensors objects,
    factory design pattern
    """
    @staticmethod
    def createSensor(sensorType, numberStr, plane):
        """
        method for dynamic creation of Sensors object, from given type name
        :param sensorType: a string, sensor type name
        :param numberStr: string, number of sensor
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: Sensor class object
        """
        if sensorType == 'EngineTempSensor':
            return EngineTempSensor(sensorType + numberStr, plane)
        elif sensorType == 'EngineFuelSensor':
            return EngineFuelSensor(sensorType + numberStr, plane)
        elif sensorType == 'AltitudeSensor':
            return AltitudeSensor(sensorType + numberStr, plane)
        elif sensorType == 'TimeSensor':
            return TimeSensor(sensorType + numberStr, plane)
        elif sensorType == 'PressureSensor':
            return PressureSensor(sensorType + numberStr, plane)
        elif sensorType == 'WheelsONOFF':
            return WheelsONOFF(sensorType + numberStr, plane)

    @staticmethod
    def createSensorList(sensorsDict, plane):
        """
        automatically generates list of Sensors objects
        :param sensorsDict: a dict, {'type_of_sensor':quantity}
        :param plane: a Plane class object,
            used for access to simulation parameters
        :return: list of Sensors class objects
        """
        l = []
        for sensorName in sensorsDict.keys():
            for i in range(sensorsDict[sensorName]):
                l.append(SensorFactory.createSensor(sensorName, '#'+str(i+1), plane))
        return l

"""
def ConstructSensorDict(listOfSensors):

    dict = {}
    for sensor in listOfSensors:
        dict[sensor.getName()] = sensor
    return dict
"""
