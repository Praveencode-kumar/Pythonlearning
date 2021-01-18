'''Exercise 15.1. Write a function called distance_between_points that takes two Points as arguments and returns the distance between them.'''


def distance_between_points(x,y):
    a=abs(x[0]-y[0])
    b=abs(x[1]-y[1])
    c=(x**2+y**2)**.5
    return c


