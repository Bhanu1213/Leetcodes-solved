class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s=="":return t
        to=0;diff=0
        for i in s:
            to+=ord(i)-ord("a")
        for i in t:
            diff+=ord(i)-ord("a")
        return chr(diff-to+ord("a"))

        