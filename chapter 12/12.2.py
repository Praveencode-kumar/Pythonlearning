
#Exercise 12.2

import random

with open('words.txt') as fd:
    words = fd.read().splitlines()


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
        t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

print sort_by_length(words)