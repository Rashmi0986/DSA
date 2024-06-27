def longest_valid_substring(s):
    max_len = 0
    max_substr = ""
    current_substr = ""
    i = 0
    
    for i in range(len(s)):
        current_substr += s[i]
        # Check for more than two contiguous occurrences
        if len(current_substr) >= 3 and current_substr[-1] == current_substr[-2] == current_substr[-3]:
            # Update the longest substring if the current one is longer
            if len(current_substr) - 1 > max_len:
                max_len = len(current_substr) - 1
                max_substr = current_substr[:-1]
            # Reset current_substr to the last two characters
            current_substr = current_substr[-2:]

    # Final check after the loop
    if len(current_substr) > max_len:
        max_len = len(current_substr)
        max_substr = current_substr
        
    return max_substr
# Test the function
test_str = "aabbaaaabb"
result = longest_valid_substring(test_str)
print(f"The longest valid substring is: {result}")
