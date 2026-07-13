class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        inc=len(str(low))
        i=0
        res=[]
        num=0
        while inc<=len(str(high)):
            if i+inc>9:
                inc+=1
                i=0
                continue
            num=int(s[i:inc+i])
            if num>high:
                break
            elif num>=low:
                res.append(num)
            i+=1
        return res


        




            


        
            


        
        