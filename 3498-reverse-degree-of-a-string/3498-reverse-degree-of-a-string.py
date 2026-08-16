class Solution:
    def reverseDegree(self, s: str) -> int:
        ma=0
        for i,ch in enumerate(s,start=1):
            k=123-ord(ch)
            ma+=k*i
        return ma
        