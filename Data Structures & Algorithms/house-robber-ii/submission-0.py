class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob_linear(nums: List[int]) -> int:
            incl, excl = 0, 0
            for n in nums:
                max_rob = max(incl + n, excl)
                incl = excl
                excl = max_rob
            return excl
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))