#26. Remove Duplicates from Sorted Array 20190523

class Solution:
    def removeDuplicates(self, nums) -> int:
        '''check = []
        #ans = 0
        for i in range(0, len(nums)):
            if(nums[i] not in check):
                check.append(nums[i])
        return len(check)'''       
        '''if not nums:return 0
        len_list = len(nums)
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1'''
        if(not nums):
            return 0
        j = 0
        for i in range(1, len(nums)):
            if(nums[i] != nums[j]):
                nums[j+1] = nums[i]
                j = j+1
        return j+1 

self = Solution()
nums = [1,1,2,3]
print(self.removeDuplicates(nums))