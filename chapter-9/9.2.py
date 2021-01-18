fin = open('words.txt')

def has_no_e(word):
    for char in word:
        if char in 'Ee':
            return False
    return True  

count = 0
for line in fin:
    word = line.strip()
    if has_no_e(word):
        count += 1
        print (word)

percent = (count / 113809.0) * 100

print (str(percent)) + "% of the words don't have an 'e'."