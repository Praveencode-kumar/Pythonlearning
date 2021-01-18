# =============================================================================
# 
# Exercise 14.3. If you download my solution to Exercise 12.4 from http: // thinkpython. com/
# code/ anagram_ sets. py , you’ll see that it creates a dictionary that maps from a sorted string of
# letters to the list of words that can be spelled with those letters. For example, 'opst' maps to the
# list ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
# Write a module that imports anagram_sets and provides two new functions: store_anagrams
# should store the anagram dictionary in a “shelf;” read_anagrams should look up a word and return
# a list of its anagrams.
# =============================================================================


import pickle

def anagrams_sets(wlist):
    d=dict()
    for word in wlist:
        a=list(word)
        a.sort()
        a=tuple(a)
        d[a]=d.get(a,[])+[word]
    return d

def stored_anagrams(d):
    a=raw_input('read or write ')    
    if a == 'write':
        f=open('yoga.db','w')
        f.write(pickle.dumps(d))
    elif a=='read':
        f=open('yoga.db')
        s=''.join(f.readlines())
        s=pickle.loads(s)
        for x in s:
            d[x]=s[x]
    f.close()
