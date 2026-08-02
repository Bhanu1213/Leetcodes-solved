class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        bor=0
        nums=set(nums)
        for i in nums:
            if i&1==0: bor|=i
        return bor
        