class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==k: return sum(nums)/k 
        cur=sum(nums[:k])
        ma=cur
        for i in range(k,len(nums)):
            cur+=nums[i]-nums[i-k]
            ma=max(cur,ma)
        return ma/k


        