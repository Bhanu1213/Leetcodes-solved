class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        k=list(d.values())
        return all(k[i]==k[0] for i in range(len(k)))

        