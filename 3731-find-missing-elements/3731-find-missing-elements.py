class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # return [i for i in range(min(nums),max(nums)) if i not in nums]
        se=set(nums)
        s=min(nums)
        m=max(nums)
        mis=[]
        for i in range(s+1,m):
            if i not in se:
                mis.append(i)
        return mis

        