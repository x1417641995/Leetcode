#67. Add Binary
#finish

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''tem = int(a) + int(b)
        ans = 0
        print(tem)
        i = 1
        while(tem > 0):
            if(tem%10 == 2):
                tem = tem + 10
                ans = ans + ((tem%10) - 2) * i
            else:
                ans = ans + (tem%10) * i            
            i = i*10
            tem = int(tem/10)                        
        return str(ans)'''
        '''
        eval() is get srt value
        0b means binary string
        '''
        return bin(eval("0b"+a)+eval("0b"+b))[2:]

self = Solution()
a = "11"
b = "1"
print(self.addBinary(a, b))