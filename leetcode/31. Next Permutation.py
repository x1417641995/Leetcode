# 31. Next Permutation 20190603
#finish

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-1, 0, -1):
            if(nums[i] > nums[i-1]):

                self.listsort(nums, i)
                for j in range(i, len(nums)):
                    if(nums[i-1] < nums[j]):
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                break
            if(i < 2):
                nums = nums.sort(reverse=False)
                #print(i)
                
    def listsort(self, nums, a):
        #a = a + 1
        l = len(nums)
        for i in range(a, a+((len(nums)-a)//2)):
            nums[i], nums[l - 1] = nums[l - 1], nums[i]
            l = l-1 
            
self = Solution()
print(self.nextPermutation([0,5,3,4,]))
            