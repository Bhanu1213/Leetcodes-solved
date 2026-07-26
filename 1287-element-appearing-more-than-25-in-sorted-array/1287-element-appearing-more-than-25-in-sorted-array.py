class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        for i in arr: d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]>=len(arr)/4:
                ma=i
        return ma
            
        