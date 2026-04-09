class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        n=len(nums)
        output=[1]*n
        for i in range(n):
            output[i]*=left
            left*=nums[i]
        right=1
        for i in range(n-1,-1,-1):
            output[i]*=right
            right*=nums[i]
        return output