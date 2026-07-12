class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        te=sorted(set(arr))
        d={};res=[]
        i=1
        for j in te:
            d[j]=i
            i+=1
        return [d[i] for i in arr]
