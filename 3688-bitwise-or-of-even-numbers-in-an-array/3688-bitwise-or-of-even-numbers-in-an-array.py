class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        bor=0
        for i in nums:
            if i&1==0: bor|=i
        return bor
        