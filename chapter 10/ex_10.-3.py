#Write a function called chop that takes a list, modifies it by removing the first and
#last elements, and returns None


def chop(list1):
    del list1[0]
    del list1[-1]


list2 = [1, 2, 3, 4]
chopped_list = chop(list2)
print(list2)                          
print(chopped_list) 