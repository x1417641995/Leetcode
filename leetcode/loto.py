def solution(A, B, C):
    # write your code in Python 3.6
    a, b, c = "a", "b", "c"
    lista = [A, B, C]
    
    #print(lista)
    
    #print(lista.index(max(lista)))
    ans = ""
    sum = A+B+C
    couna, counb, counc = 0, 0, 0
    for i in range(0, sum):
        if(lista.index(max(lista)) == 0 and couna < 2):
            ans = ans+a
            lista[0] = lista[0]-1
            couna = couna+1
        elif(lista.index(max(lista)) == 1 or couna>=2):
            ans = ans+b
            lista[1] = lista[1]-1
            couna = 0
            counb = counb+1
            counc = 0
        elif(lista.index(max(lista)) == 2 or couna>2 or counb>2):
            ans = ans+c
            lista[2] = lista[2]-1
            couna = 0
            counb = 0
    print(ans)
    return ans
    pass
solution(6, 1, 1)  
    