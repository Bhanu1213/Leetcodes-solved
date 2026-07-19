class Solution:
    def reverseVowels(self, s: str) -> str:
        vo="aeiouAEIOU"
        l=0;r=len(s)-1
        res=list(s)
        while l<r:
            if res[l] in vo and res[r] in vo:
                res[l],res[r] = res[r],res[l]
                l+=1;r-=1
            elif res[l] not in vo:l+=1
            elif res[r] not in vo:r-=1
        return "".join(res)




        