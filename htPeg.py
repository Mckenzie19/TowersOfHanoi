#Towers of Hanoi Peg Class
from htDisk import Disk

class Peg(object):

    def __init__(self, pegNum=0, diskList=[]):
        self.pegNum=pegNum
        self.__diskList=diskList

    def setDiskList(self):
        for a in self.__diskList:
            if a.getCurrentPeg()!=self.pegNum:
                del a
        return self.__diskList

    def getDiskList(self):
        return self.__diskList

    def getNumDisks(self):
        numDisks=self.__diskList
        return len(numDisks)

    def moveDisk(self, idx=0):
        disk=self.__diskList[idx]
        del self.__diskList[idx]
        return disk

    def addDisk(self, disk):
        self.__diskList.insert(0, disk)
        disk.setCurrentPeg(self.pegNum)

    def __str__(self):
        return 'Peg '+str(self.pegNum)

    def __repr__(self):
        return 'Peg '+str(self.pegNum)
