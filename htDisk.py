#Towers of Hanoi Disk Class

class Disk(object):

    def __init__(self, currentPeg=0, size=0):
        self.__currentPeg=currentPeg
        self.__size=size

    def getCurrentPeg(self):
        return self.__currentPeg

    def getSize(self):
        return self.__size

    def setCurrentPeg(self, pegNum):
        self.__currentPeg=pegNum

    def getName(self):
        return 'Disk '+str(self.__size)

    def __repr__(self):
        return 'Disk '+str(self.__size)

    def __str__(self):
        return 'Disk '+str(self.__size)
