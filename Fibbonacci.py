def Fib(x):
    if(type(x) == type(1) and x > 0):
        if(x == 1 or x == 2):
            return 1
        return Fib(x - 1) + Fib(x - 2)
    else:
        return "Error"
    
