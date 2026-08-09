class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0;r=len(nums)-1
        concat=0
        while l<=r:
            if l!=r:
                t=int(str(nums[l])+str(nums[r]))
                concat+=t
                l+=1
                r-=1
            else:
                concat+=nums[l]
                l+=1
                r-=1
        return concat

        