class Solution:
    def rob(self, nums: List[int]) -> int:
        incl,excl=0,0
        for n in nums:
            max_rob=max(incl+n,excl)
            incl=excl
            excl=max_rob
        return max_rob
        