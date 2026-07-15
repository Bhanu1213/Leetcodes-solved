class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        sum1=0
        while num>0:
            sum1+=num%10
            num//=10
        return sum1 if sum1<10 else self.addDigits(sum1)

        
        