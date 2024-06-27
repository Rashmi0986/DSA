
"""
Microsoft Online Assessment (OA) - Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a subsequence of arr which has unique characters. Return the maximum possible length of s.

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
Example 1:

Input: ["un","iq","ue"]

Output: 4
"""
from typing import List
2def maxLength(arr: List[str]) -> int:
3      maxlen = 0
4      unique = ['']
5
6      def isvalid(s):
7          return len(s) == len(set(s))
8
9      for word in arr:
10          for j in unique:
11              tmp = word + j
12              if isvalid(tmp):
13                  unique.append(tmp)
14                  maxlen = max(maxlen, len(tmp))
15
16      return maxlen
17
18if __name__ == "__main__":
19    word_list = input().split()
20    print(maxLength(word_list))
