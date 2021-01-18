# =============================================================================
# 
# '''Exercise 15.2. Write a function named move_rectangle that takes a Rectangle and two numbers
# named dx and dy. It should change the location of the rectangle by adding dx to the x coordinate of
# corner and adding dy to the y coordinate of corner.'''
# 
# =============================================================================

def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy


