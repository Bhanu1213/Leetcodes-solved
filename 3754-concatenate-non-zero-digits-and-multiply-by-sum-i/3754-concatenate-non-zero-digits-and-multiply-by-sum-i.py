class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0: return 0
        sum1=0
        k=str(n).replace("0","")
        while n>0:
            a=n%10
            if a!=0:
                sum1+=a
            n//=10
        return sum1*int(k)