class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={};res=[]
        for i in nums:
            if i in d:
                res.append(i)
            d[i]=d.get(i,0)+1
        k=set(nums)
        for i in range(1,len(nums)+1):
            if i not in k:res.append(i)
        return res 
        