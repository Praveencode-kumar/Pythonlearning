
# =============================================================================
# Exercise 11.10. Two words are “rotate pairs” if you can rotate one of them and get the other (see
# rotate_word in Exercise 8.12).
# Write a program that reads a wordlist and finds all the rotate pairs.'''
# 
# =============================================================================

def make_dict(file_input):
    diction = dict()
    word_list = []

    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)

    index = 0
    for word in word_list:
        diction[word] = index
        index += 1
    return diction


def rotate_word(word, shift):
    rotate = ''
    for let in word:
        rotate += chr(ord(let) + shift)
    return rotate


def rotate_pairs(word_dict):
    pairs = {}
    for let in range(1, 27):
        for word in word_dict:
            if rotate_word(word, let) in word_dict:
                if word in pairs:
                    pairs[word].append((rotate_word(word, let), let))
                else:
                    pairs[word] = [(rotate_word(word, let), let)]
    return pairs


diction = make_dict("words.txt")
print(rotate_pairs(diction))



