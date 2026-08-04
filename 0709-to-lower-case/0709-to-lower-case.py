class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        l=""
        for i in s:
            if i.isupper():
                l+=chr(ord(i)+32)
            else:l+=i
        return l
        