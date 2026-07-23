class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2: return n
        t0=0;t1=t2=1
        for i in range(2,n):
            t0,t1,t2=t1,t2,t0+t1+t2
        return t2
        