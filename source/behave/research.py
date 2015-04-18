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
        self.__vehicle = "Sedan"
        self.__drive_speed = None
        self.__hdd_speed = 0
        self.__latency = 0
        self.__city_origin = None

    @property
    def city_origin(self):
        return self.__city_origin
    @city_origin.setter
    def city_origin(self, x):
        self.__city_origin = x
        
    @property
    def latency(self):
        return self.__latency
    @latency.setter
    def latency(self, x):
        self.__latency = x
        
    @property
    def hdd_speed(self):
        return self.__hdd_speed
    @hdd_speed.setter
    def hdd_speed(self, x):
        self.__hdd_speed = x
        
    @property
    def drive_speed(self):
        return self.__drive_speed
    @drive_speed.setter
    def drive_speed(self, x):
        self.__drive_speed = x
        
    @property
    def vehicle(self):
        return self.__vehicle
    @vehicle.setter
    def vehicle(self, x):
        self.__vehicle = x
        
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
        with open(path, 'r') as f:
            lines = f.readlines()
            for a in lines:
                self.__city.append(a.split())
                
    def writeDataToFile(self, path):
        with open(path, 'w') as f:
            for a in self.__city:
                f.write("%s %s %s\n" % (a[0], a[1], a[2]))
     
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
                
        speed = int(temp[1])
        if self.__drive_speed != None:
            speed = self.__drive_speed
    
        if self.computeDriveTimeInMinutes(int(temp[1]), speed) < self.computeNetworkTimeInMinutes():
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