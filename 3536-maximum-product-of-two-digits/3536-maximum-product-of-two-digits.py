class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while n>0:
            a=n%10
            l.append(a)
            n//=10
        l=sorted(l)
        return l[-1]*l[-2]