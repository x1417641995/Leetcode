#12. Integer to Roman 20190325

class Solution:
    def intToRoman(self, num: int) -> str:
        roman =""
        R = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        N = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(0, len(R)):
            while(num >= R[i]):
                num = num - R[i]
                roman = roman + N[i]
        return roman        
        '''# M = 1000
        M = num//1000
        for i in range(0, M):
            roman = roman + "M"
        num = num % 1000
        # D = 500 C = 100
        C = num//100'''
        
