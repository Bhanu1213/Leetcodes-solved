class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        k=[]
        for i,num in enumerate(nums):
            if num>target:break
            elif num==target:k.append(i)
        return k 
        