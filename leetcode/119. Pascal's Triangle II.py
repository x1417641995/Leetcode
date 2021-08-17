
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        last = [1, 1]
        for i in range(1, rowIndex):
            new = [1]
            for j in range(0, len(last)-1):
                new.append(last[j] + last[j+1])
            new.append(1)
            last = new
        return last