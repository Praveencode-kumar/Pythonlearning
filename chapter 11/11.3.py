
#Exercise 11.3

def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def print_hist(histogram):
    histoList = histogram.keys()
    histoList.sort()
    for letter in histoList:
        print letter, histogram[letter]

h = histogram('parrot')
print_hist(h)

