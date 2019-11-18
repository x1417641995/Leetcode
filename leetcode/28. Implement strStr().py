#28. Implement strStr() 20190527

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
                
        return  haystack.find(needle)
    
self = Solution()
#haystack = [1,1,2,3]
haystack = "helloll"
needle = "ll"

print(self.strStr(haystack, needle))