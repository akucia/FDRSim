from time import clock
from math import *

class Plane(object):

    def __init__(self,name,x,y,z,vx,vy,vz):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx              # km/s
        self.vy = vy               # km/s
        self.vz = vz
        self.g = 0.01
        self.t0 = 0
        self.inAir = False
        self.t = 0

    def getName(self):
        return self.name

    def takeoff(self):
        self.t0 = clock()
        self.inAir = True

    def update(self):
        if self.inAir:
            self.t = clock() - self.t0
            t = self.t
            self.x = self.vx * t
            self.y = self.vy * t
            self.z = self.vz * t - self.g / 2 * t**2

    def getPosition(self):
        return [self.x, self.y, self.z]

    def getTime(self):
        return self.t

    def getVelocity(self):
        t = self.t
        v2 = self.vx**2 + self.vy**2 + (self.vz + self.g*t)
        return sqrt(v2)

    def hasLanded(self):
        return not(self.inAir)

    def isFlying(self):
        return self.inAir
