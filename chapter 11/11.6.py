
#Exercise 11.6

known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    else:
        res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res

#def fibonacci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci(40)


