#70. Climbing Stairs 20190915
#finish

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a+b
        return a 