#Brute force approach 
class Solution:
    #ref link - https://leetcode.com/problems/restore-ip-addresses/solutions/3079093/python3-simple-brute-force-solution/
    def works(self, s):
        return s == str(int(s)) and int(s) <= 255 and int(s) >= 0

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if self.works(a) and self.works(b) and self.works(c) and self.works(d):
                        ans.append(f'{a}.{b}.{c}.{d}')
        return ans


#backtracking

#https://iq.opengenus.org/generating-ip-addresses/

class Solution:
    def __init__(self):
        self.res = []
        self.segment = []
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtrack(s, 0, self.segment, self.res)
        return self.res
        
    def backtrack(self, s: str, idx: int, segments: List[str], res: List[str]) -> None:
        if len(segments) == 4 and idx == len(s):
            res.append('.'.join(segments))
            return
        
        if len(segments) < 4 and idx < len(s):
            # try inserting some numbers to segments
            for i in range(1, 4):
                if idx + i > len(s):
                    break
                seg = s[idx:idx+i]
                if self.isvalid(seg):
                    segments.append(seg)
                    self.backtrack(s, idx+i, segments, res)
                    segments.pop()
                    
    def isvalid(self, s: str) -> bool:
        if len(s) > 1 and s[0] == '0':
            return False
        val = int(s)
        return val >= 0 and val <= 255


if __name__ == '__main__':
    s = Solution()
    input_str = "29347125"
    valid_id = s.restoreIpAddresses(input_str)
    for id in valid_id:
        print(id)



"""
Simple approach from neetcode (do reffer )
https://www.youtube.com/watch?v=61tN4YEdiTM
"""
