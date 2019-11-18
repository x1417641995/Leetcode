#13. Roman to Integer 20190331

class Solution:
    def romanToInt(self, s: str) -> int:
        R = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        N = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        dict = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40,
                "X":10, "IX":9, "V":5, "IV":4, "I":1}
        number = dict[s[0]]
        for i in range(1, len(s)):
            
            if(dict[s[i-1]] < dict[s[i]]):
                number = number + dict[s[i]] - dict[s[i-1]]*2
                i = i+1
            else:
                number = number + dict[s[i]]    
            
        return number    

self = Solution()
print(self.romanToInt("IV"))