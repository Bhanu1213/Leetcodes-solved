class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            sum1=0
            while i>0:
                a=i%10
                sum1+=a
                i//=10
            if sum1%2==0:
                count+=1
        return count

        