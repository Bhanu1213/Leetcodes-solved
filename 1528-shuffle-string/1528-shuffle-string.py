class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        se=[0]*len(indices)
        k=0
        for i in indices:
            se[i]=s[k]
            k+=1
        return "".join(se)
