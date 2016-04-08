from time import clock
from math import *

class Plane(object):
    """
    class for simulation of movement of a "plane",
    which behaves like a ballistic missile
    """
    def __init__(self, vx, vy, vz, name="rocket", x=0, y=0, z=0):
        """
        initialization
        :param vx: a float, initial velocity in x axis direction (km/s)
        :param vy: a float, initial velocity in y axis direction (km/s)
        :param vz: a float, initial velocity in z axis direction (km/s)
        :param name: a string, name for the plane, default is "rocket"
        :param x: a float, initial position i x axis direction, default is 0
        :param y: a float, initial position i y axis direction, default is 0
        :param z: a float, initial position i y axis direction, default is 0
        :return:
        """
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx              # velocities in km/s
        self.vy = vy
        self.vz = vz
        self.g = 0.01
        self.t0 = 0
        self.inAir = False
        self.t = 0

    def getName(self):
        """

        :return: a string, name of the plane
        """
        return self.name

    def takeoff(self):
        """
        begins the simulation, resets the clock
        :return: none
        """
        self.t0 = clock()
        self.inAir = True

    def update(self):
        """
        updates the planes position
        :return:
        """
        if self.inAir:
            self.t = clock() - self.t0
            t = self.t
            self.x = self.vx * t
            self.y = self.vy * t
            self.z = self.vz * t - self.g / 2 * t**2
        if self.z < 0:
            self.inAir = not self.inAir

    def getPosition(self):
        """

        :return: a list of floats, current position of a plane
        """
        return [self.x, self.y, self.z]

    def getTime(self):
        """

        :return: a float, internal clocks time
        """
        return self.t

    def getVelocity(self):
        """
        returns value of plane's initial velocity (lenght of a 3d vector)
        :return: a float, plane's velocity
        """
        t = self.t
        v2 = self.vx**2 + self.vy**2 + (self.vz + self.g*t)
        return sqrt(v2)

    def isFlying(self):
        """
        checks if a plane is still above the ground level
        :return: a boolean,
        """
        return self.inAir
