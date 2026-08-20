class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        ar=[nums[0]]
        ar1=[nums[1]]
        for i in range(2,len(nums)):
            if ar[-1]>ar1[-1]:ar.append(nums[i])
            else: ar1.append(nums[i])
        return ar+ar1
