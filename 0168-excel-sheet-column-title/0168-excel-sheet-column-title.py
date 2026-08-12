class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        re=''
        while columnNumber>0:
            columnNumber-=1
            r=columnNumber%26
            re+=chr(ord("A")+r)
            columnNumber//=26
        return re[::-1]
        