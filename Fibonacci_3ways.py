def fib(n):
  if n <=1 :
    return n
  return fib(n-1)+fib(n-2)
 
print(fib(3))

"""
Problem  with the above solution:
Now how to avoid the recomputation in the above recursion tree 
Solution 1: Use the fib_memozation
"""

def fib_Memo(n, memo):
    
    if n <=1:
        return n 
    if n not in memo:
        memo[n] = fib_Memo(n-1, memo) + fib_Memo(n-2, memo)
        
    return memo[n]
    

memo = {0:0, 1:1}
print(fib_Memo(2, memo))

"""
#Reason am using the dictionary for the memo is get/set/del takes O(1) Time complexity 
But the above algorithm takes the O(N) time complexity 
How to reduce that ?

#Use the for loop with the one variable solution 
"""
def fibOptimised(n):
  if n<=1:
    return n 
    
  f0 = 0
  f1 = 1
  for i in range(2,n+1):
    fib = f0 + f1
    f0 = f1
    f1 = fib

  return fib 


"""
Tested and optimised
"""









  
