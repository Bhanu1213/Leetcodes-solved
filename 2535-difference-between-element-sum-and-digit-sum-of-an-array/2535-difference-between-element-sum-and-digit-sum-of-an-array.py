class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digitsum(k):
            su=0
            while k>0:
                a=k%10
                su+=a
                k//=10
            return su
        su=0
        for i in nums:
            if i>=10:su+=digitsum(i)
            else:su+=i
        return abs(sum(nums)-su)
        