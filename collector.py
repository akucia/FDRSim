from Plane import Plane
from Sensors import SensorFactory
from Buffer import Buffer
from Log import Log, encoder

def collector(sensorsDict):
# TODO delete imports for collector function, it's not used anymore
    #initialization

    plane = Plane('rocket',0,0,0,0.5,0.2,2.5)           # velocities in km/s
    sensors = sensorsDict
    sensorsList = SensorFactory.createSensorList(sensors, plane)

    buffer = Buffer(10)
    plane.takeoff()                                     # start the simulation
    n = 0

    while plane.isFlying() and n < 10:                  # until it touches the ground
        plane.update()
        buffer.readData(sensorsList)

        n += 1
    header = encoder(sensorsList)
    print(header)
    buffer.printData()

    Log.saveToCSV(plane.getName(),header,buffer.returnDataCopy())
