
#Exercise 11.4

def reverse_lookup(dictionary, value):
    results = []
    for key in dictionary:
        if dictionary[key] == value:
            results.append(key)
    return results


def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

h = histogram('parrot')
k = reverse_lookup(h, 2)
print (k)
