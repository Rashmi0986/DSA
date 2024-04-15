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


