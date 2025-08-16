#Interview Tips 
"""
Rule of thumb

Start with the set approach → because it’s intuitive, easy to explain, and shows you understand the sliding window pattern.

Then pivot to the hashmap approach → because it’s more optimal and eliminates the need for a while loop.

This way, you demonstrate:

Clarity of thought (start with the simple brute/sliding-window idea).

Ability to optimize (move to hashmap once interviewer asks about performance).

🔹 How to position them in the interview
1.Naive substring-building approach,
 How it works:

 Keeps a string subStr representing the current window.

 If char c is not in subStr, append it.

 If c already exists, split subStr at c and rebuild it from the part after c + c.
 🔹 Contribution of subStr to I/O

Here, I/O means string operations cost (since strings in Python are immutable).

c not in subStr → O(k) scan (k = window size).

subStr.split(c) → O(k) traversal + creates a list of substrings.

String concatenation (+) → O(k) because a new string must be allocated.

So every iteration does multiple passes over subStr, which is expensive.

Worst-case: O(n²) time, O(n) space.

For large inputs (say, 10⁵ characters), this will choke

2. Set Approach (with while loop)

Explain:

“I’ll maintain a sliding window with start and end, and a set to keep track of the characters inside the window. If a duplicate comes in, I’ll shrink the window from the left until the duplicate is removed.”

Pros: Easy to implement, shows understanding of window shrinking.

Cons: In worst case, start moves step by step (O(2n)).

3. Hashmap Approach (with if condition)

Explain:

“Instead of shrinking step by step, I can use a hashmap to record the last index of each character. That way, when I see a duplicate, I can jump start directly to the index after the last occurrence. This guarantees O(n) time.”

Pros: Optimal, cleaner (no while loop), O(n) guaranteed.

Cons: Slightly trickier to reason about, but that’s why it’s the follow-up.


🔹 Comparison with other approaches
Approach           	                Data structure	                    Duplicate handling	           Complexity	         Space	Notes
Substring (subStr)	                String buffer	                       Split + rebuild	             O(n²) worst	O(n)	  Simple to write, inefficient for long strings
Set + while	                        Set + two pointers	                 Shrink step by step	         O(2n) ~ O(n)	O(k)	  Easy to explain, sliding window pattern
Hashmap + if	                      Dict + two pointers	                 Jump directly	               O(n)	O(k)	          Most efficient, no redundant removals

"""
class Solution:
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = ""
        maxLen = 0
        for c in s:
            if c not in subStr:
                subStr+=c
                maxLen = max(maxLen , len(subStr))
            else:
                subStr = subStr.split(c)[1]+c
        return maxLen
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        maxlen = 0 
        for end in range(len(s)):
            while s[end] in seen:
              seen.remove(s[start])
              start+=1
            seen.add(s[end]) 
            maxlen = max(maxlen, end - start+1)
        return maxlen      
        
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        maxLength = 0 
        start = 0
        for end ,char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = end # insert at end - irrespective of the char found or not.
            maxLength = max(maxLength , end - start +1)
        return maxLength
    
        
             
