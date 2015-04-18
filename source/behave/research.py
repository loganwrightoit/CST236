"""
Research
"""

class Research(object):
    """
    Research Class
    """
	
    def __init__(self):
        self.__mbps = 0
        self.__hdd_size = 0
        self.__city = []

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, x):
        self.__city = x
        
    @property
    def mbps(self):
        return self.__mbps
    @mbps.setter
    def mbps(self, x):
        self.__mbps = x

    @property
    def hdd_size(self):
        return self.__hdd_size
    @hdd_size.setter
    def hdd_size(self, x):
        self.__hdd_size = x

    def readDataFromFile(self, path):
        f = open(path)
        lines = f.readlines()
        f.close()
        for a in lines:
            self.__city.append(a.split())
        
    def computeDriveTimeInMinutes(self, dist_mi, speed_mph):
        return float(dist_mi) / float(speed_mph) * 60
        
    def computeNetworkTimeInMinutes(self):
        MB = float(self.__hdd_size * 1000)
        MBps = float(self.__mbps) / 8
        return MB / MBps / 60
        
    def computeFastestMethod(self, inCity):
        temp = []
        for a in self.__city:
            if a[0] is inCity:
                temp = a
                break
    
        if self.computeDriveTimeInMinutes(int(temp[1]), int(temp[2])) < self.computeNetworkTimeInMinutes():
            return "Driving"
        else:
            return "Network"
        
    def computeTimeDiff(self, city):
        temp = []
        for a in self.__city:
            if a[0] == city:
                temp = a
                break
        time1 = self.computeDriveTimeInMinutes(int(temp[1]), int(temp[2]))
        time2 = self.computeNetworkTimeInMinutes()
        return abs(time1 - time2)