"""
String Without 3 Identical Consecutive Letters
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
