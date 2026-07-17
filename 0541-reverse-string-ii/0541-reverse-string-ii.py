class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        st=''
        i=0;b=0
        while i<len(s):
            j=s[i:k+i]
            if b%2==0:
                st+=j[::-1]
            else:
                st+=j
            i+=k
            b+=1
        return st
            
        