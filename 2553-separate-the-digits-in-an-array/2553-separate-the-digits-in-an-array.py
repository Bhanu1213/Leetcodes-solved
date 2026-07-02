class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res1=[]
        for i in nums:
            res=[]
            while i>0:
                a=i%10
                res.insert(0,a)
                i//=10
            res1+=res
        return res1

        