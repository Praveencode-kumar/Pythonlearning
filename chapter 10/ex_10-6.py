#Write a function called is_sorted that takes a list as a parameter and returns True
#if the list is sorted in ascending order and False otherwise.

def is_sorted(list1):
    if sorted(list1) == list1:
        return True
    else:
        return False


print(is_sorted([1, 2, 3, 4, 5]))