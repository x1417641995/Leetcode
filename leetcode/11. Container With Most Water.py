#11. Container With Most Water20190324


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max = 0
        a = 0
        b = len(height)-1
        for i in range(0, len(height)):
            if(height[a] > height[b]):
                #c = height[b]*(len(height)-1-i)
                if(max < height[b]*(len(height)-1-i)):
                    max = height[b]*(len(height)-1-i)
                b = b-1
            else:
                #c = height[a]*(len(height)-1-i)
                if(max < height[a]*(len(height)-1-i)):
                    max = height[a]*(len(height)-1-i)
                a = a+1
        return max     
self1 = Solution()
list=[1,2,5]

print(self1.maxArea(list))