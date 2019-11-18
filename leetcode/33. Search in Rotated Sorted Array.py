#33. Search in Rotated Sorted Array 20190605
#finish

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (target in nums):
            return nums.index(target)
        else:
            return -1