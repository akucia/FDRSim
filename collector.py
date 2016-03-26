from Plane import Plane
from Sensors import *


def collector():
    #initialization
    SensorFactory()
    plane = Plane('rocket',0,0,0,0.5,0.2,2.5)           # velocities in km/s
    sensors = {"EngineTempSensor": 4,"EngineFuelSensor": 4, "AltitudeSensor": 1, "PressureSensor": 1}
    sensorsList = SensorFactory.createSensorList(sensors, plane)
    for sensor in sensorsList:
        print(sensor.getName() + '\t\t' + str(sensor.read()))
    #buffer = Buffer(10)
    #log = Logger()

    #plane.takeoff()                                     # start the simulation

    while(plane.isFlying()):                            # until it touches the ground
        # gathering data
        pass





    #call for buffer and logger

