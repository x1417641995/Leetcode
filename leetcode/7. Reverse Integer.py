#7. Reverse Integer 20190322

x=123
def reverse(self, x: int) -> int:
    self.x = x
    c = True
    if(x<0):
        x = -x
        c = False
    ans = 0
    while(x>0):
        ans = x%10 +ans*10
        x = x//10
    if(c == False):
        ans = - ans
    if(ans >= 2**31 - 1 or ans <= - 2**31):
        return 0
    else:
        return ans
        
    

print(x)   