def Factorial(x) :
    if x == 0 :
        Result = 1
    else :
        Result = x * Factorial(x-1)
    return(Result)

print(Factorial(3))
