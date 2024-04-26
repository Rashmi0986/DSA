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
