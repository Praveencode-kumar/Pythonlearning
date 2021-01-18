

#Exercise 10.10.

def version1(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)

    return li


def version2(file):
    fin = open(file)
    t = []

    for line in fin:
        x = line.strip()
        t = t + [x]
