class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            a=k*(i+1)
            if a not in nums:
                return a
        return k*(len(nums)+1)
        
        