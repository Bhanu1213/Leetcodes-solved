class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            pr=1
            for i in str(n):
                pr*=int(i)
                if pr%t==0:
                    return n
            n+=1
            
        
        