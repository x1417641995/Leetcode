
#137. Single Number II
# finish
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if(d.get(nums[i]) == None):
               d[nums[i]] = 1
               continue
            d[nums[i]] =  d[nums[i]] + 1
        for k, v in d.items():
            if(v == 1):
                return k

self = Solution()
nums = [2,2,3,2]
print(self.singleNumber(nums))