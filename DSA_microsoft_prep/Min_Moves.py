#Min Moves to Make String Without 3 Identical Consecutive Letters
def minMoves(s):
    res = 0 
    size = len(s)
    for i in range(size):
        n = i+1
        while n < size and s[i] == s[n]:
            n += 1
        res+=(n - i) // 3
    return res
    
    
s = "baaaab"
print(minMoves(s))


"""
for the above same problem to get the exact string 
def filter_string(s: str) -> str:
    news = s[0:2]
    for i in range(2, len(s)):
        # Do not append if the previous chars are the same
        if s[i] != s[i - 1] or s[i] != s[i - 2]:
            news += s[i]
    return news

if __name__ == '__main__':
   s = input()
   res = filter_string(s)
   print(res)
"""

Ref
https://molchevskyi.medium.com/microsoft-interview-tasks-min-moves-to-make-string-without-3-identical-consecutive-letters-abe61ed51a10


