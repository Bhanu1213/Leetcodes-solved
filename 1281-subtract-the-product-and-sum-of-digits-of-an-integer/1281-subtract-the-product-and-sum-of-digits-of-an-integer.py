class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        div=1;sum1=0
        while n>0:
            a=n%10
            sum1+=a
            div*=a
            n//=10
        return div-sum1
        