

#Exercise 14.2

import os

cwd = os.getcwd()

for one, two, three in os.walk(cwd):
    print one, three




