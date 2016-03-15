from Plane import Plane
from Sensors import *



rocket = Plane("rakieta",0,0,0)

ETS = EngineTempSensor("ETS")
EFS = EngineFuelSensor("EFS")
AS = AltitudeSensor("AS")
rocket.takeoff()
rocket.move()
rocket.move()
sensorsDict = ConstructSensorDict([ETS,EFS,AS])
while rocket.isFlying():
    print(rocket.position())
    rocket.move()
    for key in sensorsDict.keys():
        print (sensorsDict[key].read())



