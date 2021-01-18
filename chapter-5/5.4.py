
#Exercise 5.4.
#If you are given three sticks, you may or may not be able to arrange them in
#a triangle. For example, if one of the sticks is 12 inches long and the other
#two are one inch long, you will not be able to get the short sticks to meet in
#the middle.  For any three lengths, there is a simple test to see if it is
#possible to form a triangle:


def is_triangle(a, b, c):
    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("Yes")


def prompting():
    a = input("Type length of side a: ")
    b = input("Type length of side b: ")
    c = input("Type length of side c: ")

    is_triangle(int(a), int(b), int(c))


prompting()




