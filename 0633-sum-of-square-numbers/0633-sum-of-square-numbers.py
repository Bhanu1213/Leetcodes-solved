import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=round(math.sqrt(c))
        while l<=r:
            cur=l**2+r**2
            if cur==c:return True
            elif cur<c:l+=1
            else: r-=1
        return False
        
        