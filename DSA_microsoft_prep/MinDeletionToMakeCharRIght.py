"""
#Min Deletions To Obtain String in Right Format

Given a string with only characters X and Y. Find the minimum number of characters to remove 

from the string such that there is no interleaving of character X and Y and all the Xs appear before any Y.

Example 1:

Input:YXXXYXY

Output: 2

Explanation:

We can obtain XXXYY by:

Delete first Y -> XXXYXY
Delete last occurrence of X -> XXXYY
"""
2def minStep(str) -> int:
3      charX = 'X';
4      numY = 0;
5      minDel = 0;
6      for i in range(0, len(str)):
7          if (charX == str[i]):
8              minDel = min(numY, minDel + 1);
9          else:
10              numY = numY + 1;
11      return minDel;
12if __name__ == '__main__':
13    print(minStep(input()))
