class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        div=len(nums)
        mul=0
        for i in range(1,div+1):
            if div%i==0:mul+=nums[i-1]**2
        return mul