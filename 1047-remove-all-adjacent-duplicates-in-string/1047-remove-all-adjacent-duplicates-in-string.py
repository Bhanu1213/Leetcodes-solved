class Solution:
    def removeDuplicates(self, s: str) -> str:
        st="";i=0
        while i<len(s):
            if st and st[-1]==s[i]:
                st=st[:-1]
            else: st+=s[i]
            i+=1
        return st
        