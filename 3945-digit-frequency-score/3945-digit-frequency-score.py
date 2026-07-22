class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n=str(n)
        d={}
        r=0
        for i in n:
            d[i]=d.get(i,0)+1
        for key,val in d.items():
            r+=int(key)*val
        return r

        