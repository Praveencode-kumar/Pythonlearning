
#Two words are “rotate pairs” if you can rotate one of them and get the other 
#Write a program that reads a wordlist and finds all the rotate pairs



from rotate import rotate_word


def word_dict():
    d = dict()
    fn = open('words.txt')
    for line in fn:
        word = line.strip().lower()
        d[word] = word
 
    return d


def rotate_pairs(word, word_dict1):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict1:
            print(word, i, rotated)


word_dict1 = word_dict()

for word in word_dict1:
    rotate_pairs(word, word_dict1)