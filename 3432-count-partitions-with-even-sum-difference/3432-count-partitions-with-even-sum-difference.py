class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l=0
        total=sum(nums)
        count=0
        for i in range(len(nums)-1):
            l+=nums[i]
            r=total-l
            diff=abs(l-r)
            if diff%2==0:count+=1
        return count

        