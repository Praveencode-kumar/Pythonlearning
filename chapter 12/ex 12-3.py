
#ex :12.3
# Write a function called most_frequent that takes a string and prints the letters
# in decreasing order of frequency. Find text samples from several different languages and see
# how letter frequency varies between languages


text = 'hello, what a plesant surprise!'


def new_dict(x):
    d = {}
    for letter in x:
        d[letter] = 1 + d.get(letter, 0)
    return d


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = new_dict(letters)
    result = []
    for key in d:
        result.append((d[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)


most_frequent(text)