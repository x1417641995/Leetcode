#22. Generate Parentheses 2019-05-20
    
def generateParenthesis(n): 
    ans = []        
    def fun(a = "", left = 0, right = 0):
        print(a)
        if(len(a) == n*2):
            ans.append(a)
            #return
        if(left < n):
            fun(a +"(", left +1, right)
        if(right < left):
            fun(a +")", left, right +1)
    fun()
    
    return ans        
            
print(generateParenthesis(7))