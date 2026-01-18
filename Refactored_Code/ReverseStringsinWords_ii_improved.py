class Solution:
    def reverseWords(self, input_str):
        """
        Reverses the order of words in a string.
        
        Algorithm: Two-step reversal approach
        1. Reverse each individual word in place
        2. Reverse the entire string
        Result: Word order is reversed, but words remain intact
        
        Example:
            Input:  "the sky is"
            Step 1: "eht yks si" (each word reversed)
            Step 2: "is yks eht" (entire string reversed)
            But since words were already reversed, they become normal again!
            Output: "is sky the"
        
        Args:
            input_str (str): Input string with words separated by spaces
            
        Returns:
            str: String with words in reversed order
            
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(n) for converting string to list
        """
        # Edge case: empty or None string
        if not input_str:
            return input_str
        
        # Edge case: single word (no spaces)
        if ' ' not in input_str:
            return input_str
            
        def reverse(chars, start, end):
            """Helper function to reverse characters in place between indices."""
            while start < end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        
        # Convert string to list for in-place modification
        chars = list(input_str)
        word_start, current, length = 0, 0, len(chars)
        
        # Step 1: Reverse each word individually
        while current < length:
            if chars[current] == ' ':
                # Found end of word, reverse it
                reverse(chars, word_start, current - 1)
                word_start = current + 1
            elif current == length - 1:
                # Last word in string
                reverse(chars, word_start, current)
            current += 1
        
        # Step 2: Reverse the entire string
        reverse(chars, 0, length - 1)
        
        return ''.join(chars)


# ============================================
# UNIT TESTS
# ============================================
def test_reverse_words():
    """Comprehensive test suite for reverseWords function"""
    solution = Solution()
    
    # Test 1: Normal case
    assert solution.reverseWords("the sky is") == "is sky the", "Failed: Normal case"
    print("✓ Test 1 passed: Normal case")
    
    # Test 2: Two words
    assert solution.reverseWords("hello world") == "world hello", "Failed: Two words"
    print("✓ Test 2 passed: Two words")
    
    # Test 3: Single word
    assert solution.reverseWords("hello") == "hello", "Failed: Single word"
    print("✓ Test 3 passed: Single word")
    
    # Test 4: Empty string
    assert solution.reverseWords("") == "", "Failed: Empty string"
    print("✓ Test 4 passed: Empty string")
    
    # Test 5: Single character
    assert solution.reverseWords("a") == "a", "Failed: Single character"
    print("✓ Test 5 passed: Single character")
    
    # Test 6: Multiple words
    assert solution.reverseWords("a b c d") == "d c b a", "Failed: Multiple words"
    print("✓ Test 6 passed: Multiple words")
    
    # Test 7: Words with different lengths
    assert solution.reverseWords("I love Python") == "Python love I", "Failed: Different lengths"
    print("✓ Test 7 passed: Words with different lengths")
    
    print("\n✅ All tests passed!")


# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    # Run tests
    print("Running test suite...\n")
    test_reverse_words()
    
    # Demo examples
    print("\n" + "="*50)
    print("DEMO EXAMPLES")
    print("="*50)
    
    solution = Solution()
    test_cases = [
        "the sky is",
        "hello world",
        "Python is awesome",
        "a",
        ""
    ]
    
    for test in test_cases:
        result = solution.reverseWords(test)
        print(f'Input:  "{test}"')
        print(f'Output: "{result}"')
        print()
