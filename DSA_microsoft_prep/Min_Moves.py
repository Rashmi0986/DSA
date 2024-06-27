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

Ref
https://molchevskyi.medium.com/microsoft-interview-tasks-min-moves-to-make-string-without-3-identical-consecutive-letters-abe61ed51a10



    
