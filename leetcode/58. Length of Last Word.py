#58. Length of Last Word 20190829
# Finish
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.strip().split(" ")
        return len(ans[-1])
    
self = Solution()
s = "Hello World"
print(self.lengthOfLastWord(s))