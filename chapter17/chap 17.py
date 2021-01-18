# ex 17.2
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    

    def print_point(self):
        print("x =", self.x, ",",)
        print("y =", self.y)


point = Point()
point.print_point()

point = Point(20, 30)
point.print_point()



#ex 17.4

def add_mtd(self,z);
    self.z = z
    z = Point.x + Point.y
    return z

print(z)