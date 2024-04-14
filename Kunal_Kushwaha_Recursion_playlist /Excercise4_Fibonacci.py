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
        self.assertEqual(ValueError, func(-sys.maxsize+1))
        # Execution halts with the Value Error
        """
        print("All Tests Passed : Test run Complete !!")
    

if __name__ == "__main__":
    Test = TestFibonacci()
    FibObj = Fibonacci()
    Test.TestFib(FibObj.Fib)


