# sliding window maximum
from collections import deque
class Solution(object):
    def add_to_dq(self, dq, nums, i):
        while len(dq) and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        return

    def maxSlidingWindow(self, nums, k):
        
        if k == 0:
            return []
        dq = deque()
        for i in range(k):
            self.add_to_dq(dq, nums, i)
        result, start, end = [], 0, k-1
        while end < len(nums):
            while True:
                if dq[0] >= start:
                    result.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            start, end = start+1,end+1
            if end < len(nums):
                self.add_to_dq(dq, nums, end)
        return result