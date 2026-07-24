class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            sum1=0
            while n>0:
                a=n%10
                sum1+=a**2
                n//=10
            n=sum1
        return n==1
        

        