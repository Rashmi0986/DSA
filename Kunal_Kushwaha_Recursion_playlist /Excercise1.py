#Problem Statement 
"""

you need to call one function but the function has to print the message mutiple times 

Multiple ways to solve the problem 

1. Call the function in the for loop - O(1) Space , O(N) TC 
2. Use the  recursion technique  - O(N) - space , O(N) Time complexity 

Lets try to use the second technique
"""

def msg1():
    print("Hello world !")
    msg2()

def msg2():
    print("Hello world !")
    msg3()

def msg3():
    print("Hello world !")
    msg4()

def msg4():
    print("Hello world !")
    msg5()

def msg5():
    print("Hello world !")

if __name__ == "__main__":
    msg1()




