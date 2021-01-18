

#Exercise 11.8

listOne = [1, 2, 3, 4, 5, 5]


def has_dups(myList):
    dictionary = {}
    for item in myList:
        dictionary[item] = 1 + dictionary.get(item, 0)
        if dictionary[item] > 1:
            return True
    return False

print (has_dups(listOne))


