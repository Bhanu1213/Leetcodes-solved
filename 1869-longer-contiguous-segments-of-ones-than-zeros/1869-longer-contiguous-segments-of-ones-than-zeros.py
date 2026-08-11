class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        c0=0
        c1=0
        count=0
        pre=""
        for i in s:
            if pre!=i:count=0
            if i=="1":
                count+=1
                if c1<count:c1=count
            else:
                count+=1
                if c0<count:c0=count
            pre=i
        return c0<c1