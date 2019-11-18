#36. Valid Sudoku 20190617
#finish
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(0, 9):
            checkcol = []
            checkrow = []
            for j in range(0, 9):
                #column check
                if(board[i][j] in checkcol and board[i][j] != "."):
                    #print(i, j)
                    return False
                checkcol.append(board[i][j])
                #row check
                if(board[j][i] in checkrow and board[j][i] != "."):
                    #print("row")
                    return False
                checkrow.append(board[j][i])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = []
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        if(board[m][n] in check and board[m][n] != "."):
                            #print("b")
                            return False
                        check.append(board[m][n])
        return True
                        
                    