#Exercise 11.1

import uuid

with open('words.txt') as fd:
    words = fd.read().splitlines()

result = dict()


def dictionary():
    for line in words:
        result[line] = uuid.uuid4()
    return result

print (dictionary())


