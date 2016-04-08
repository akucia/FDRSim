from copy import deepcopy
from time import clock


class Buffer(object):
    """
    class for reading and buffering data
    from objects of Sensor class
    """
    def __init__(self, freq, sensorList):
        """
        initialization, calculation of period of data acquisition
        :param freq: a float, frequency of data acquisition
        :param sensorList: list of sensors used in simulation
        :return:
        """
        self.sensorList = sensorList
        self.freq = freq
        self.allReadings = []
        self.allReadingsHorizontal = []
        self.time = clock()
        self.period = float(1)/float(self.freq)
        for i in range(len(sensorList)):
            list = []
            self.allReadingsHorizontal.append(list)

    def readData(self):
        """
        reads data from active sensors
        :return: None
        """

        while clock() - self.time < self.period:
            pass
        self.time = clock()
        buffer = []
        i = 0
        for sensor in self.sensorList:
            buffer.append(sensor.read())
            self.allReadingsHorizontal[i].append(sensor.read())
            i += 1
        self.allReadings.append(buffer)

    def returnDataCopy(self):
        """
        returns data list, where each sublist consists
        of readings from all sensors at given step
        returns safe copy of buffered data (not a reference!)
        :return: copy of buffered data
        """
        return deepcopy(self.allReadings)

    def returnDataTr(self):
        """
        returns data list, where each sublist
        consists of readings from different sensor
        :return: transposed table of buffered data
        """
        return self.allReadingsHorizontal

    def printData(self):
        """
        prints data stored inside buffer
        :return: none
        """
        for line in self.allReadings:
            for number in line:
                print (number, '\t',end=" ")
            print()
