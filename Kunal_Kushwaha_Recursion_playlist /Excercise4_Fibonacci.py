"""
Fibonacci and reccurence relation 
Fib(n) = Fib(n-1) + Fib(n-2)

"""

def Fib(n):
    if n == 0 or n == 1:
        return n
    return Fib(n-1) + Fib(n-2)

if __name__ == "__main__":
    print(Fib(5))


