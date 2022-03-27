#https://leetcode.com/problems/valid-parentheses/


#3 ways to solve this problem 
"""
1. Using hashMap and List 
2. Using string.replace method(built-in ) lib 
3. Using Just stack 
"""

# method 1 - TC = O(N), SC = O(N)
class Solution:
    def isValid(self, s: str) -> bool:
     
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
        
        
        
        
        
    # method 2. - TC = O(N) , SC = O(1)
    class Solution:
      def isValid(self, s: str) -> bool:

          """
          :type s: str
          :rtype: bool
          """
          x=1
          while x>0:
              i = len(s)
              s = s.replace('()','').replace('[]','').replace('{}','')
              x = i-len(s)
          return i==0
        
    # Method 3 - requires TC = O(N) SC= O(N)
    
    class Solution:
      def isValid(self, s: str) -> bool:

          """
          :type s: str
          :rtype: bool
          """

          stack = []
          for c in s:
              if len(stack):
                  if (c == ")" and stack[-1] == "(") \
                  or (c == "]" and stack[-1] == "[") \
                  or (c == "}" and stack[-1] == "{"):
                      stack.pop()
                      continue
              stack.append(c)
          return len(stack) == 0
        
    
