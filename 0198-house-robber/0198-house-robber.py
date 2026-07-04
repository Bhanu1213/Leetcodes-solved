class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        for num in nums:
            temp=max(sum2,sum1+num)
            sum1=sum2
            sum2=temp
        return sum2


        