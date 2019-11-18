#34. Find First and Last Position of Element in Sorted Array 20190625
#finish

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        if (target in nums):
            ans.append(nums.index(target))
            a = nums.index(target)
            nums.pop(nums.index(target))
            if (target in nums):                
                ans.append(nums.index(target)+1)
                nums.pop(nums.index(target))
                i = 2
                while(target in nums):
                    ans[1] = nums.index(target)+i
                    nums.pop(nums.index(target))
                    i = i+1
                return ans
            else:
                return [a, a]
        else:
            return [-1, -1]