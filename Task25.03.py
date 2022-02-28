CallNumber = 0
def Factorial(x) :
    global CallNumber
    CallNumber +=  1
    print(""""--------""",x,"""--------""")
    print(""""--------""",CallNumber,"""--------""")
    if x == 0 :
        Result = 1
    else :
        Result = x * Factorial(x-1)
        print('Result: ', Result)
    return(Result)

print(Factorial(4))