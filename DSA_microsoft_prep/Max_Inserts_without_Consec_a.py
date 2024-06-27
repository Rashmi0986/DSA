Max Inserts to Obtain String Without 3 Consecutive ‘a’​.

  

  def solution(s):
    count_a = 0 
    count_others = 0
    s_len = len(s)
    for c in s:
        if c == "a":
            count_a+=1 
        else:
            count_others+=1 
        if count_a == 3:
            return -1 
    return 2 * (count_others + 1) - (s_len - count_others)
    
print(solution("bab"))
