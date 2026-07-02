class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum1=0
        i=len(str(n))-1
        n=int(n)
        while n>0:
            a=n%10
            if i%2==0:sum1+=a
            else: sum1-=a
            n//=10
            i-=1
        return sum1
        
        