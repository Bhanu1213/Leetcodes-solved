class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow={"a","e","i","o","u"}
        cur=sum(1 for i in range(k) if s[i] in vow)
        maxi=cur
        for i in range(k,len(s)):
            if s[i] in vow:
                cur+=1
            if s[i-k] in vow:
                cur-=1
            if cur>maxi:
                maxi=cur
        return maxi
            

            

            