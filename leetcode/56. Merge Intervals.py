# 56. Merge Intervals 20190828
#
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        a = 0
        for i in range(0, len(intervals)-1 ):
            print(i)
            if(intervals[i][1] >= intervals[i+1][0]):
                ans.append([intervals[i][0], intervals[i+1][1]])
                a +=1
            else:
                ans.append(intervals[i+a])
            print(ans)        
        if not ans:
            ans.append(intervals)
        return ans
    
self = Solution()
num = [[1,3],[2,6],[8,10],[15,18]]
nums = [[1,3]]
num2 = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
num3 = [-2,1,-3,4,-1,2,1,-5,4]

print(self. merge(num2))