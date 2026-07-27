class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic={}
        res=[]
        sv=sorted(nums)
        for i,val in enumerate(sv):
            if val not in dic:
                dic[val]=i
        for num in nums:
            res.append(dic[num])
        return res

        