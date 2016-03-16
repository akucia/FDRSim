from time import clock
from math import *

class Plane(object):

    def __init__(self,name,x,y,z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.Vx = 0.5               # km/s
        self.Vy = 0.2               # km/s
        self.Vz = 2.5
        self.t0 = clock()
        self.g = 0.01

    def __name__(self):
        return self.name

    def takeoff(self):

        self.t0 = clock()

    def move(self):
        t = clock() - self.t0
        self.x = self.Vx * t
        self.y = self.Vy * t
        self.z = self.Vz * t - self.g / 2 * t**2

    def position(self):
        return [self.x, self.y, self.z]

    def velocity(self):
        t = clock() - self.t0
        v2 = self.Vx**2 + self.Vy**2 + (self.Vz + self.g*t)
        return sqrt(v2)

    def isFlying(self):
        if self.z > 0:
            return True
        else:
            return False
