#9. Palindrome Number20190323
x= 121

def isPalindrome(x: int) -> bool:
    x = list(str(x))
    #x = list(map(int,x))
    results = True
    l = len(x)-1
    
    for i in range(0, len(x)//2):
        #prin
        if( x[i] != x[ l- i]):
            results = False
     
    return results



print(isPalindrome(x))