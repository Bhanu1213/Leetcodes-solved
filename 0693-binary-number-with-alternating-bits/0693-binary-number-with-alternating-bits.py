class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # pre=-1;k=0
        # while n>0:
        #     a=n%2
        #     if pre==a:
        #         return False
        #     pre=a
        #     k=k*10+a
        #     n//=2
        # return True
        x=n^(n>>1)
        return x&(x+1)==0
        
        