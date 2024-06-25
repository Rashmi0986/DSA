def letter_combination(n: int) -> List[str]:
    res = []

    def dfs(path=[]):
        if len(path) == n:
            res.append("".join(path))
            return

        for letter in "ab":
            path.append(letter)
            dfs(path)
            path.pop()

    dfs()
    return res

def letter_combination(n):
    res = []

    def dfs(path=[]):
        if len(path) == n:
            res.append("".join(path))
            return

        for letter in "123":
            path.append(letter)
            dfs(path)
            path.pop()

    dfs()
    return res
    
print(letter_combination(3))

['111', '112', '113', '121', '122', '123', '131', '132', '133', '211', '212', '213', '221', 
 '222', '223', '231', '232', '233', '311', '312', '313', '321', '322', '323', '331', '332', '333']


#Similarly for generate valid Parentheses

def is_valid(s , n):
    """
    for each closing paren, check for preceding open paren 
    """
    open_count, closed_count = 0, 0
    for c in s:
        if c == '(':
            open_count += 1
        elif c == ')':
            closed_count += 1
        
        if closed_count > open_count:
            return False 
        if open_count > n:
            return False

def traverse(state, path):
        if state == 2*n:
            res.append(''.join(path))
        
        for bracket in ['(', ')']:
            path.append(bracket)
            if is_valid(path,n):
                traverse(state+1, path)
            path.pop()       
    traverse(0, [])       
    
    return res

