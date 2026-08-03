class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        max_int=0x7FFFFFFF
        while b!=0:
            soc=(a^b)&mask
            car=((a&b)<<1)&mask
            a=soc
            b=car
        return a if a<=max_int else ~(a^mask)
        