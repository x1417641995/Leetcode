#66. Plus One 20190911
# finish
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if(digits[i] < 9):
                digits[i] = digits[i]+1
                break
            elif(i == 0 and digits[i]):
                digits[i] = 0
                digits.insert(0, 1)
            else:    
                digits[i] = 0
        return digits    
    
self = Solution()
digits = [5,5,4,3]
print(self.plusOne(digits))