def uses_only(word, letters):
       for letter in word:
        if letter not in letters:
            return False
    return True