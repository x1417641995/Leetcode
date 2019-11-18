from itertools import product
from itertools import permutations
import itertools
def solution(A):
    # write your code in Python 3.6
    cost = len(A)*2
    cost2 = 0
    a2 = 0
    
    
    if(cost > 25):
        cost = 25
        
    for i in range(0, len(A)):
        a = A[a2]
        b = A[i]
        if( b-a >5):
            if(i-a2 >3):
                print(a2, i)
                cost2 = cost2 -2*(i-a2+1)
                cost2 = cost2 + 7
                a2 = i+1
                
            else:    
                a2 = a2+1
            
        cost2 = cost2 +2
        print(cost2, "X")
    if(cost > cost2):
        cost = cost2
        
    return cost 
print(solution([1,4,6,7,8,9,10,14,15]))
c = ""
a = "a"
b = "b"
c = a+b
print(c)

str1 = ["flower","flow","flight"]
print(min(str1, key = len))
print(min(str1))
print(str1)

a2019 = 3
nums = [0,3,1,5,1]
del nums[4]
print(nums)
print(nums.index(1), 222)



def strStr(haystack: str, needle: str) -> int:
        a20 = haystack.find(needle)
        a21 = haystack.find(needle)
        print(a20, a21)
        return  a21
    
haystack = "helloll"
needle = "ll"

print(strStr(haystack, needle))
print(strStr(haystack, needle))


l2 = [1, 2, 3]
words = ["dhvf","heqg","cpwo","gdcj","lnle"]
list1 = list(permutations(words, len(words)))
#print(list1, len(list1))
'''b = 4 in l2
if(b == False):
    print((4) in l2)'''


nums = [1, 2, 7, 4, 3, 3]
print(nums.index(3,1), "index")
if 2 in nums[2:5]:
    print("嘿嘿嘿")
nums.pop()
a = nums.pop()

print(a, 4)
print(nums)
def listsort(nums, a):
    #nums = [1, 2, 8,7, 4, 3, 1]
    #a = a + 1
    l = len(nums)
    for i in range(a, ((len(nums)-a)//2)):
        nums[i], nums[l - 1] = nums[l - 1], nums[i]
        l = l-1
    return nums
nums9 = [5,6,7,8]
perm = permutations(nums9, len(nums9))

    
for i in range(len(nums9)):
    print(nums9[:i], nums9[i+1:])
    print(nums9[:i]+nums9[i+1:])
#print(listsort(nums, 2))

