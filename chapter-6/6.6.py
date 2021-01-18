


'''ex:6.6:  A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the
middle is a palindrome.'''



'''def fir(word):
    return word[0]


def las(word):
    return word[-1]


def mid(word):
    return word[1:-1]


def palindrome(word):
    if len(word) <= 1:
        return True
    if fir(word) != las(word):
        return False
    return palindrome(mid(word))


print(palindrome('sister'))
print(palindrome('MOM'))
print(palindrome('Brother'))
print(palindrome('python'))'''

