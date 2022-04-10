
# 136. Single Number
# finish
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if(d.get(nums[i]) == None):
               d[nums[i]] = True
               continue
            del  d[nums[i]]
        for key in d.keys():
            return key

self = Solution()
nums = [2,2,1]
print(self.singleNumber(nums))