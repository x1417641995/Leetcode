

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(0, target, candidates, [], 0, ans, 0)
        return ans
        
    def dfs(self, s, target, list, sub, i, ans, b):
        if(i >= len(list)):
            if sub:
                a = sub.pop()
                b = list.index(a) +1
                print(b,"dfs1 same", sub)
                if b in list[i+1:len(list)]:
                    print(b)
                    return self.dfs(s-a, target, list, sub, list.index(a, b, len(list))+1, ans, b)
                else:
                    return self.dfs(s-a, target, list, sub, list.index(a)+1, ans, b)
            return
        else:
            s = s + list[i]
            sub.append(list[i])
            if(s == target):
                print(sub, "=")
                ans.append(sub.copy())
                print(ans)
                return self.dfs2(s, target, list, sub, i+1, ans, b)
            elif(s < target):
                print(sub, "<")
                return self.dfs(s, target, list, sub, i+1, ans, b)
            elif(s > target):
                print(sub, ">")
                s = s - sub.pop()
                if not sub:
                    print("not")
                    return self.dfs(s, target, list, sub, i+1, ans, b)
                else:
                    #print(sub)
                    a = sub.pop()
                    b = list.index(a) +1
                    print(b,"dfs1 1")
                    if b in list[i+1:len(list)]:
                        print(b)
                        return self.dfs(s-a, target, list, sub, list.index(a, b+1, len(list))+1, ans, b)
                    else:
                        print(b,"dfs1 2")
                        return self.dfs(s-a, target, list, sub, list.index(a)+1, ans, b)
        
    def dfs2(self, s, target, list, sub, i, ans, b):           
        s = s - sub.pop()
        if not sub:
            return 
        a = sub.pop()
        b = list.index(a) + 1
        print(b, "dfs2 1")
        if b in list[i+1:len(list)]:
            print(b)
            return self.dfs(s-a, target, list, sub, list.index(a, b, len(list))+1, ans, b)
        else:
            return self.dfs(s-a, target, list, sub, list.index(a)+1, ans, b)
        
self = Solution()
candidates =[1,2,2]
target = 4
print(self.combinationSum2(candidates, target))