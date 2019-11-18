#39. Combination Sum 20190626
#finish
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(0, target, candidates, [], 0, ans)
        return ans
        
    def dfs(self, s, target, list, sub, i, ans):
        if(i >= len(list)):
            if sub:
                a = sub.pop()
                return self.dfs(s-a, target, list, sub, list.index(a)+1, ans)
            return
        else:
            s = s + list[i]
            sub.append(list[i])
            if(s == target):
                ans.append(sub.copy())
                #print(ans)
                return self.dfs2(s, target, list, sub, i, ans)
            elif(s < target):
                #print(sub, "<")
                return self.dfs(s, target, list, sub, i, ans)
            elif(s > target):
                #print(sub, ">")
                s = s - sub.pop()
                if not sub:
                    return self.dfs(s, target, list, sub, i+1, ans)
                else:
                    #print(sub)
                    a = sub.pop()
                    return self.dfs(s-a, target, list, sub, list.index(a)+1, ans)
        
    def dfs2(self, s, target, list, sub, i, ans):           
        s = s - sub.pop()
        if not sub:
            return 
        a = sub.pop()       
        return self.dfs(s-a, target, list, sub, list.index(a)+1, ans)
self = Solution()
candidates =[2,3,5]
target = 8
print(self.combinationSum(candidates, target))
               