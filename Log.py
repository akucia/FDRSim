import time
import os


class History(object):
    """
    contains methods for creating and maintaining log
    """
    def __init__(self):
        """
        creates empty list for future logs
        :return: none
        """
        self.storage = []

    def add(self, newItem):
        """

        :param newItem: list, contains strings which will be added to history
        :return: none
        """
        self.storage.append(newItem)

    def show(self):
        """
        prints on screen all entries from history
        :return: none
        """
        print("History:")
        for item in self.storage:
            print(item)

    def saveToFile(self):
        """
        saves history to file
        :return: none
        """
        directory = os.getcwd() + '/history'
        if not os.path.exists(directory):                   # checks if directory exists
            os.makedirs(directory)
        fileName = directory + '/' + time.strftime("%H:%M:%S") + '.txt'      # creates new file name using current time

        logFile = open(fileName,'a')                        # opens or creates file
        for item in self.storage:
            logFile.write(item)
            logFile.write('\n')

        print("Log saved to" + fileName)

    def isEmpty(self):
        """
        checks if history is empty
        :return:
        """
        if len(self.storage) == 0:
            return True
        else:
            return False


