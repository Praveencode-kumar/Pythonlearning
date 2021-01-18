
'''Exercise 15.3. Write a version of move_rectangle that creates and returns a new Rectangle
instead of modifying the old one.'''

import copy
def move_rectangle(rect,dx,dy):    
    a=copy.deepcopy(rect)
    a.corner.x+=dx
    a.corner.y+=dy
    return a
