def smallest_string(s: str) -> str:
2    for i in range(len(s) - 1):
3        if s[i] > s[i + 1]:
4            break
5    return s[:i] + s[i + 1:]
6
7if __name__ == '__main__':
8    s = input()
9    res = smallest_string(s)
10    print(res)
11
