class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):return False
        d={}
        for p,w in zip(pattern,words):
            k_p=("p",p)
            k_w=("w",w)
            if k_p in d and d[k_p]!=w:
                return False
            if k_w in d and d[k_w]!=p:
                return False
            d[k_p]=w
            d[k_w]=p
        return True 
            
        
        