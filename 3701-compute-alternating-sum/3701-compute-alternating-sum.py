class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        k=nums[0]
        for i in range(1,len(nums)):
            if i%2==0:
                k+=nums[i]
            else:k-=nums[i]
        return k
            
        