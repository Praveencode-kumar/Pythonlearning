
#Exercise 5.6.
#The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
#curve with length x, all you have to do is


import turtle
bob = turtle.Turtle()

def koch(turtle, length):
    if length < 3:
        turtle.fd(length)
        return
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)
    turtle.rt(120)
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)

def snowflake(turtle, length):
    for i in range(3):
        koch(turtle, length)
        turtle.rt(120)

koch(bob, 30)

bob.pu()
bob.fd(50)
bob.pd()

snowflake(bob, 30)

turtle.mainloop()

