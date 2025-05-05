Template code 


def backtrack(path, options):
    if end_condition(path):
        result.append(path[:])  # Make a copy
        return
    
    for option in options:
        if is_valid(option, path):
            path.append(option)
            backtrack(path, options)
            path.pop()  # Undo the move


@Subsets problem 
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
