class Solution:
    def replaceDigits(self, s: str) -> str:
        cur=""
        res=""
        for i in s:
            if i.isalpha():
                res+=i
                cur=i
            else:
                res+=chr(ord(cur)+int(i))
        return res

        