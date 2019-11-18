# 14. Longest Common Prefix 20190403
# by Ta-Ju

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if(len(strs) == 0):
            return ans
        else:
            l = len(min(strs, key = len))
            check = True
            j = 0
            for i in range(0, l):
                for j in range(0, len(strs)-1):
                    if(strs[j][i] != strs[j+1][i]):
                        check = False
                        break
                if(check):
                    ans = ans + strs[j][i]    
            return ans

