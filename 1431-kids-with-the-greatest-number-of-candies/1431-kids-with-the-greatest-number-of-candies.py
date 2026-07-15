class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        max1=max(candies)
        for i in candies:
            res.append(i+extraCandies>=max1)
        return res