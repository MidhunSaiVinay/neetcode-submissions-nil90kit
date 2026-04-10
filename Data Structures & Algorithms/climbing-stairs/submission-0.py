class Solution:
    def climbStairs(self, n: int) -> int:
        prev=1
        prev2=1
        if n<=2:
            return n
        for i in range(n-1):
            curr=prev+prev2
            prev2=prev
            prev=curr
        return curr