#27. Remove Element 20190523

class Solution:
    def removeElement(self, nums, val):
        j = 0
        for i in range(0, len(nums)):
            if(nums[i] != val):
                #nums[i] = nums[i+1]
                nums[j] = nums[i]
                j = j+1  
                              
        return j
            
        
        
        
self = Solution()
nums = [1,1,2,3]
print(self.removeElement(nums, 1))