from Plane import Plane
from Sensors import *
from Buffer import Buffer

def collector():
    #initialization
    SensorFactory()
    plane = Plane('rocket',0,0,0,0.5,0.2,2.5)           # velocities in km/s
    sensors = {"TimeSensor": 1, "EngineTempSensor": 4,"EngineFuelSensor": 4, "AltitudeSensor": 1, "PressureSensor": 1}
    sensorsList = SensorFactory.createSensorList(sensors, plane)

    buffer = Buffer(10)
    #log = Logger()

    plane.takeoff()                                     # start the simulation
    n = 0
    while plane.isFlying() and n < 10:                            # until it touches the ground
        plane.update()
        buffer.readData(sensorsList)

        n += 1
    header = []
    for s in sensorsList:
        header.append(s.getName())
    print(header)
    buffer.printData()
    print("___________________")

