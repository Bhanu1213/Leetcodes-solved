class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in nums:
            while i>0:
                a=i%10
                if a==digit:
                    count+=1
                i//=10
        return count