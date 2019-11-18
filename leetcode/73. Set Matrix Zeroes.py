# 73. Set Matrix Zeroes 20191003
# finish
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        z = []
        """
        find the zero in matrix
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if(matrix[i][j] == 0):
                    z.append([i, j])
        #print(z, len(z))
        """
        set zero in matrix
        """            
        for k in range(0, len(z)):
            for i in range(0, m):
                #print(m,z[k][0])
                matrix[i][z[k][1]] =0
            for j in range(0, n):
                #print(m,z[k][0])
                matrix[z[k][0]][j] =0
        return matrix        

self = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(self.setZeroes(matrix))
