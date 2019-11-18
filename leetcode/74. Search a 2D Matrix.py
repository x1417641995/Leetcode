#74. Search a 2D Matrix 20191005
# finish

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(not matrix):
            return False
        elif(not matrix[0]):
            return False
        else:
            m = len(matrix)
            n = len(matrix[0])            
            for i in range(0, m):
                if(matrix[i][-1] >= target):
                    for j in range(0, n):
                        print("b")
                        if(matrix[i][j] == target):
                            return True
                        elif(matrix[i][j] > target):
                            return False