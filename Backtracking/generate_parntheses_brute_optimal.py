"""
Contraints : while generating the parenthese
            Open == closed
            closed < open
"""

#Bruteforce code
def generate_valid_parentheses(n):
    def is_valid(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')' and stack:
                stack.pop()
            else:
                return False
        return len(stack) == 0

    def generate_all_parentheses(current, n):
        if len(current) == 2 * n:
            if is_valid(current):
                result.append(current)
            return
        generate_all_parentheses(current + '(', n)
        generate_all_parentheses(current + ')', n)

    result = []
    generate_all_parentheses('', n)
    return result

n = 3
print(generate_valid_parentheses(n))


#Optimal with backtracking method
def valid(path, n):
    counts = Counter(path)
    if counts['('] > n or counts[')'] > n or counts[')'] > counts['(']:
        return False
    return True

def generate_parentheses(n: int) -> List[str]:

    res = []
    
    def traverse(state, path):
        
        if state == 2*n:
            res.append(''.join(path))
        
        for bracket in ['(', ')']:
            path.append(bracket)
            if valid(path,n):
                traverse(state+1, path)
            path.pop()    
            
    traverse(0, [])       
    
    return res


#Space optimised  valid method 
SC = O(1), TC = O(N)
def valid(path, n)
    for char in path:
        if char == '(':
            opencount +=1
        elif char == ')':
            closecount -= 1
        if closecount > opencount:
            return False
        if open_count > n:
                return False
    return True

def generate_parentheses(n: int) -> List[str]:
    res = []
    def traverse(state, path):
        
        if state == 2*n:
            res.append(''.join(path))
        
        for bracket in ['(', ')']:
            path.append(bracket)
            if valid(path,n):
                traverse(state+1, path)
            path.pop()    
            
    traverse(0, [])       
    
    return res

