import time
import os
import os.path

class Log(object):
# TODO methods for reading from db
    """
    contains methods for creating and maintaining log
    """
    @staticmethod
    def saveToBIN(name, header, data):
        pass

    @staticmethod
    def saveToCSV(name, header, data):

        directory = os.getcwd() + '/log'
        if not os.path.exists(directory):                   # checks if directory exists
            os.makedirs(directory)
        fileName = directory + '/'+str(name)+'_' + time.strftime("%H:%M:%S") + '.csv'      # creates new file name using current time

        logFile = open(fileName,'a')                        # opens or creates file
        for item in header:
            logFile.write(item)
            logFile.write(',')

        logFile.write('\n')

        for line in data:
            for item in line:
                logFile.write(str(item))
                logFile.write(',')
            logFile.write('\n')

        logFile.close()
        print("Log saved to" + fileName)

    @staticmethod
    def saveToTXT(name, header, data):

        directory = os.getcwd() + '/log'
        if not os.path.exists(directory):                   # checks if directory exists
            os.makedirs(directory)
        fileName = directory + '/'+str(name)+'_' + time.strftime("%H:%M:%S") + '.txt'      # creates new file name using current time

        logFile = open(fileName,'a')                        # opens or creates file
        for item in header:
            logFile.write(str(item))
            logFile.write('\t')

        logFile.write('\n')

        for line in data:
            for item in line:
                logFile.write(str(item))
                logFile.write('\t')
            logFile.write('\n')

        logFile.close()
        print("Log saved to" + fileName)

    def loadDB(self):
        directory = os.getcwd() + '/log'

        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        db = []
        for file in files:
            if 'csv' in file:
                db.append(file)
        return db

    def readData(self,file):
        file = os.getcwd() + '/log/' + file
        logFile = open(file,'r')                        # opens or creates file
        line = logFile.readline()
        header = line.split(',')
        header.remove('\n')

        data = []

        for line in logFile.readlines():
            temp = line.split(',')
            temp.remove('\n')
            data.append(temp)

        newData = []
        for j in range(len(header)):
            sensor = []
            for i in range(len(data)):
                sensor.append(data[i][j])
            newData.append(sensor)

        return header, newData


def encoder(sensorsList):
    header = []
    for sensor in sensorsList:
        header.append(sensor.getName())
    return header
