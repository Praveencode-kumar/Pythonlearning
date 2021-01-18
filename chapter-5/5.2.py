def countdown(a):         # A typical countdown function
    if a < 0:
        print("Blastoff")
    elif a > 0:
        print(a)
        countdown(a - 1)

def call_function(n,a):    # The countdown function is called "n" number of times. Any other function can be used instead of countdown function.
    for i in range(n):
        countdown(a)
    
call_function(3, 10)