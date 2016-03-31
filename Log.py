import time
import os


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

def encoder(sensorsList):
    header = []
    for sensor in sensorsList:
        header.append(sensor.getName())
    return header
