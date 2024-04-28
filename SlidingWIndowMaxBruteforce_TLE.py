class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def getMax(nums, l, r, res):
            m = max(nums[l:r])
            res.append(m)

        res = []
        l = 0
        r = l + k
        n = len(nums)
        while l < r and r <= n:
            getMax(nums, l, r, res)
            l += 1
            r += 1
        return res


    
#optimal one 
class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #https://github.com/ChenglongChen/LeetCode-3/blob/master/Python/sliding-window-maximum.py
        #https://palashsharma891.medium.com/239-sliding-window-maximum-leetcode-python-6e9659b8fd2c
        q = collections.deque()
        res = []
        
        for r, n in enumerate(nums):
            while q and nums[q[-1]] <= n:
            #while q and nums[q[-1]] >= n: ->sliding window minimum
                q.pop() # keep popping from q
            q.append(r) # add only the index of the maxele
                    
            # remove 1st element if it is outside the window
            if r - q[0] == k:
                q.popleft()
                        
            # if window has k elements, add to results. this is invalid only for first k elements
            if r + 1 >= k:
                res.append(nums[q[0]])
                        
        return res

"""
Sliding window Minimum code - Simple >= change in while loop 
q = collections.deque()
        res = []
        
        for r, n in enumerate(nums):
            while q and nums[q[-1]] >= n:
                q.pop() # keep popping from q
            q.append(r) # add only the index of the maxele
                    
            # remove 1st element if it is outside the window
            if r - q[0] == k:
                q.popleft()
                        
            # if window has k elements, add to results. this is invalid only for first k elements
            if r + 1 >= k:
                res.append(nums[q[0]])
                        
        return res
"""
