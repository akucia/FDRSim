from collector import collector
from analyzer import analyzer

def FDR():
# TODO to be deleted, not used anymore
    collector({"TimeSensor": 1, "EngineTempSensor": 4,"EngineFuelSensor": 4, "AltitudeSensor": 1, "PressureSensor": 1})
    analyzer()

FDR()
