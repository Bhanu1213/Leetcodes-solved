class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        cur=nums[0]
        ma=-1
        for i in range(1,len(nums)):
            if nums[i]>cur:
                ma=max(ma,nums[i]-cur)
            else:
                cur=nums[i]
        return ma
        
        