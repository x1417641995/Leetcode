#88. Merge Sorted Array 20191113
#finish
from typing import List 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tem = nums1.copy()
        a, b = 0, 0
        for i in range(0, m+n):
            if(n == 0):
                break
            elif(n == b):
                nums1[i] = tem[a]
                a = a+1
            elif((tem[a] <= nums2[b] and a < m) ):
                nums1[i] = tem[a]
                a = a+1                
            else:
                nums1[i] = nums2[b]
                b = b+1
self = Solution()
merge = [[1,2,3,0,0,0], 3, [2,5,6], 3]
print(self.merge([1,2,3,0,0,0], 3, [2,5,6], 3))