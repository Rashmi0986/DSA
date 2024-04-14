"""
def number1():
    print(1)
    number2()

def number2():
    print(2)
    number3()

def number3():
    print(3)
    number4()

def number4():
    print(4)
    number5()

def number5():
    print(5)

if __name__ == "__main__":
    number1()

"""
#Making the above code generic here 
def number1(n):
    print(n)
    number2(n+1)

def number2(n):
    print(n)
    number3(n+1)

def number3(n):
    print(n)
    number4(n+1)

def number4(n):
    print(n)
    number5(n+1)

def number5(n):
    print(n)

if __name__ == "__main__":
    number1(n=1) # positional arguement


# The problem 
"""
The problem with the above code is we are calling the same func 
multiple times 

So how to resolve this problem ??
Call the same function with the simple variable having the different values each
time the func is called 

Recursion 


"""




