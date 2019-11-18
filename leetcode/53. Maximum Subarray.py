# 53. Maximum Subarray
# finish
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = nums[0]
        tem = ans
        for i in range(1, len(nums)):
            if(tem + nums[i] > 0 and tem >= 0):
                tem = tem + nums[i]
                if(tem > ans):
                    ans = tem        
            elif(tem < 0):
                tem = nums[i]
                if(tem > ans):
                    ans = tem
            else:               
                tem = 0
        return ans    
            
        
self = Solution()
num = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2,-1]
num2 = [1]
num3 = [-2,1,-3,4,-1,2,1,-5,4]

print(self. maxSubArray(num3))