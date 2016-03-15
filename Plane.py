from time import clock


class Plane(object):

    def __init__(self,name,x,y,z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        # maybe velocities should be added here...
    def __name__(self):
        return self.name

    def takeoff(self):
        self.Vx = 0.5    #km/s
        self.Vy = 0.2    #km/s 0,54
        self.Vz = 2.5     # 2Vz/10 = 10325
        self.t0 = clock()

    def position(self):
        t = clock() - self.t0
        self.x = self.Vx * t
        self.y = self.Vy * t
        self.z = self.Vz * t  - 0.005 * t**2
        return [self.x,self.y,self.z]

    def isFlying(self):
        if self.z > 0:
            return True
        else:
            return False


# TEST
"""
rocket = Plane("rakieta",0,0,0)

rocket.takeoff()
print(rocket.position())
print(rocket.position())
print(rocket.position())

while(rocket.isFlying()):
    print(rocket.position())
"""