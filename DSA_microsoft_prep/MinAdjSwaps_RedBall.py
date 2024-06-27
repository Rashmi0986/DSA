def min_swaps(s: str) -> int:
    reds = []
    count = 0
    for i, chr in enumerate(s):
        if chr == "R":
            reds.append(i)
    n = len(reds)
    if n == 0:
        return 0
    start_ptr = 0
    end_ptr = n - 1
    while start_ptr < end_ptr:
        count += reds[end_ptr] - reds[start_ptr] - end_ptr + start_ptr
        print(count)
        start_ptr += 1
        end_ptr -= 1
    return -1 if count > 10 ** 9 else count

if __name__ == '__main__':
    s = input()
    res = min_swaps(s)
    print(res)
