#47. Permutations II 20190806
# 
from typing import List
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(0, len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    print(new_ans)
                    if i<len(l) and l[i]==n: break 
            ans = new_ans        
        return ans
         
    
    
self = Solution()
nums = [1, 1, 3]
print(self.permuteUnique(nums))