#35. Search Insert Position 20190607
#finish
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target in nums):
            return nums.index(target)
        else:
            for i in range(0, len(nums)):
                if(nums[i]>target):
                    return i
                    break
                elif(i == len(nums)-1):
                    return i+1

self = Solution()
nums = [1,3,5,5,6]
target = 5
print(self.searchInsert(nums, target))