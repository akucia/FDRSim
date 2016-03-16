from Plane import Plane
from Sensors import *



rocket = Plane("rakieta",0,0,0)

ETS = EngineTempSensor("ETS")
EFS = EngineFuelSensor("EFS")
AS = AltitudeSensor("AS")
GPS = GPSSensor("GPS")
T = TimeSensor("T")
PS = PressureSensor("PS")
WH = WheelsONOFF("WH")
rocket.takeoff()
rocket.move()
rocket.move()
sensorsDict = ConstructSensorDict([GPS,ETS,EFS,AS,T,PS,WH])

while rocket.isFlying():
    rocket.move()
    for S in sensorsDict.keys():
       print (S + "\t" + str(sensorsDict[S].read(rocket)))
    print("---------------")



