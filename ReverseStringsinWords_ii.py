class Solution:
    def reverseWords(self, ss):
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
        i, j, n = 0, 0, len(ss)
        s = list(ss)
        while j < n:
            if s[j] == ' ':
                reverse(s, i, j - 1)
                i = j + 1
            elif j == n - 1:
                reverse(s, i, j)
            j += 1
        
        reverse(s, 0, n - 1)
        return ''.join(s)
print(Solution().reverseWords("the sky is"))
