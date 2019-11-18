#29. Divide Two Integers20190527

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend > 0 and divisor<0) or(dividend < 0 and divisor>0):
            if(dividend%divisor == 0):
                ans = (dividend//divisor)
            else:
                ans = (dividend//divisor)+1       
        else:
            ans =  dividend//divisor
        if(ans >= 2**31 - 1):
            return  2**31 - 1
        elif(ans <= - 2**31):
            return  - 2**31
        else:
            return ans
self = Solution()
dividend = -1
divisor = 1
print(self.divide(dividend, divisor))

'''elif(dividend > 0 and divisor<0):
            return (dividend//divisor)+1'''