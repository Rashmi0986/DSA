"""
Fibonacci and reccurence relation 
Fib(n) = Fib(n-1) + Fib(n-2)

"""
import sys
max_size = sys.maxsize
min_size = -sys.maxsize - 1

class Fibonacci:
    def Fib(self, n):
        if n < 0:
            return n 
        
        if n < min_size or n > max_size:
            raise ValueError("number should be valid integer")
        
        if n == 0 or n == 1:
            return n
        
        # here including the recusrion call the Extra computation is done 
        # so it is not consdiered as tail recursion .

        return self.Fib(n-1) + self.Fib(n-2)




import unittest
class TestFibonacci(unittest.TestCase):
    def TestFib(self, func):
        self.assertEqual(func(4), 3)
        self.assertEqual(func(-6), -6)
        self.assertEqual(func(1), 1)
        self.assertEqual(func(0), 0)

        """
        self.assertRaises(ValueError, func(sys.maxsize+1))
            # Execution halts with the Value Error
        self.assertRaises(ValueError, func(sys.maxsize+1))
            # Execution halts with the Value Error
        """
        print("All Tests Passed : Test run Complete !!")
    

if __name__ == "__main__":
    Test = TestFibonacci()
    FibObj = Fibonacci()
    Test.TestFib(FibObj.Fib)



#without recrusion but stack 
def fibs(n):                                                                                                 
    fibs = [0, 1, 1]                                                                                           
    for f in range(2, n):                                                                                      
        fibs.append(fibs[-1] + fibs[-2])                                                                         
    return fibs[n]


#without recursion O(1) space 

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


Variant : Study Drill - Climbing stairs
class Solution:
    def climbStairs(self,n):
        f1 = 1
        f2 = 2
        if n == 1: 
           return f1
        if n == 2:
            return f2
        else:
            i = 2 # here i made a mistake initiliasation mistake shopuld be avoided 
            while i < n:
                fib = f1 + f2
                f1 = f2
                f2 = fib
                i += 1
        return fib 

# new Solution using Fibonaccii  TC = o(n), SC = O(1)

  
        
                
   


#Some Notes :
"""
Tail recursion 

when we have last call to the print function that is called Tail recursion . 
Example below 

def myprint(n):
    if n == 5:
        print(n)
        return 
    print(n)

    #Tail Recursion 
    myprint(n+1)

if __name__ == "__main__":
    myprint(1)


Mistake :

Don't use the default print()
Lead to recusrion depth exceeded message 
"""



"""


