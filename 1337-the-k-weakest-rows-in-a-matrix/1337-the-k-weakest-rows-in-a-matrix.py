class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d={}
        for row in range(len(mat)):
            d[row]=mat[row].count(1)
        d=sorted(d,key=lambda k:d[k])
        return d[:k]
        
        