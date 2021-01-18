#Two words are anagrams if you can rearrange the letters from one to spell the other.
#Write a function called is_anagram that takes two strings and returns True if they are anagrams.

name1 = 'sadhana'
name2 = 'dharsiny'


def is_anagram(name1,name2):
    if sorted(name2) == sorted(name1):
        print('it is an anagram')
        return True
    else:
        print('it is not an anagram')
        return False


is_anagram(name1,name2)