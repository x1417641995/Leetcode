#15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(0, len(nums) - 2):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums)):
                    if(self == i + j + k):
                        a=[i, j, k]
                        a.sort()
                        ans.append(a)
        return ans                