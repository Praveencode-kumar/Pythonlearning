


#Exercise 6.5. The Ackermann function, A(m, n), is defined:
#A(m, n) =
#n + 1 if m = 0
#A(m − 1, 1) if m > 0 and n = 0
#A(m − 1, A(m, n − 1)) if m > 0 and n > 0.
#See http: // en. wikipedia. org/ wiki/ Ackermann_ function . Write a function named ack
#that evaluates Ackermann’s function. Use your function to evaluate ack(3, 4), which should be
#125. What happens for larger values of m and n?



a = 3
b = 4

def hackermann(a, b):
    if a == 0:
        return b + 1
    elif b == 0:
        return hackermann(a - 1, 1)
    else:
        print('hello')
        return hackermann(a - 1, hackermann(a, b - 1))
hackermann(8, 5)
