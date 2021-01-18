#ex 11.9


l1=[1,4,8,9,1]
def has_duplicates(l2):
    d1 ={}
    for item in l2;
        d1[item] = 1 +d1.get(item, 0)
        if d1[item] > 1:
            return True
    return False
print(has_duplicates(l1))