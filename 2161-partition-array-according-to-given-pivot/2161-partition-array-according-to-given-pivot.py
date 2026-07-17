class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sm=[];gt=[];p=[]
        for i in nums:
            if pivot>i:sm.append(i)
            elif i==pivot:p.append(i)
            else:gt.append(i)
        return sm+p+gt
        
        