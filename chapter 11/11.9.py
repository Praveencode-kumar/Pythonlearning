
# =============================================================================
# Exercise 11.9. If you did Exercise 10.8, you already have a function named has_duplicates that
# takes a list as a parameter and returns True if there is any object that appears more than once in the
# list.
# Use a dictionary to write a faster, simpler version of has_duplicates'''
# 
# =============================================================================

list = [1, 2, 3, 4, 5, 5]


def has_duplicates(myList):
    dicti = {}
    for item in myList:
        dicti[item] = 1 + dicti.get(item, 0)
        if dicti[item] > 1:
            return True
    return False

print (has_duplicates(list))


