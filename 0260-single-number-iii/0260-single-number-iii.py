class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # x=[]
        # for i in nums:
        #     if i in x:
        #         x.remove(i)
        #     else:
        #         x.append(i)
        # return x
        d={};x=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]==1:
                x.append(i)
        return x
