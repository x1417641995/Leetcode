#46. Permutations 20190806
# finish
from typing import List
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per = list(permutations(nums, len(nums)))
        return per
            
self = Solution()
nums = [1, 2, 3]
print(self.permute(nums))