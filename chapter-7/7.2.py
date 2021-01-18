

#Exercise 7.2.


def eval_loop():
    
    while True:
        user_input = input(">>> ")

        if eval(user_input) == 'done':
            break
        print(eval(user_input))

    return eval(user_input)


eval_loop()

#>>> eval('1 + 2 * 3')
#7
#>>> import math
#>>> eval('math.sqrt(5)')
#2.2360679774997898
#>>> eval('type(math.pi)')
#<class 'float'>


