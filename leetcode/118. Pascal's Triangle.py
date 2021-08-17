
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if numRows > 1:
            triangle.append([1, 1])
            last = [1, 1]
        for i in range(2, numRows):
            new = [1]
            for j in range(0, len(last)-1):
                new.append(last[j] + last[j+1])
            new.append(1)
            triangle.append(new)
            last = new
        return triangle