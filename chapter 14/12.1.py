# =============================================================================
# '''Exercise 14.1. The os module provides a function called walk that is similar to this one but more
# versatile. Read the documentation and use it to print the names of the files in a given directory and
# its subdirectories.'''
# =============================================================================

import os
import time


def run():
    direct = raw_input('name of dir ')
    flist = []
    for x, y, z in os.walk(direct):
        if len(z) > 0:
            flist.extend(z)
    print (direct)
    for x in flist:
        print (x)
        time.sleep(1)
