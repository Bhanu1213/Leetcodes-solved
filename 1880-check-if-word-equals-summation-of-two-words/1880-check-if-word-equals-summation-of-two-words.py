class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def length(s):
            r=''
            for i in s:
                r+=str(ord(i)-97)
            return r
        fi=int(length(firstWord))
        se=int(length(secondWord))
        tar=int(length(targetWord))
        return (fi+se)==tar



        