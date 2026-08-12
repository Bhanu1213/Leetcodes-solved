class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=''
        while columnNumber>0:
            columnNumber-=1
            r=columnNumber%26
            res=res+chr(ord("A")+r)
            columnNumber//=26
        return res[::-1]
        