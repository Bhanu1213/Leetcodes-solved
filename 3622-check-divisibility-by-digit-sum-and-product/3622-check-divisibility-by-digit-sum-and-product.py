class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ad=0
        x=n
        mu=1
        while n>0:
            a=n%10
            ad+=a
            mu*=a
            n//=10
        ad=ad+mu
        return x%ad==0
        