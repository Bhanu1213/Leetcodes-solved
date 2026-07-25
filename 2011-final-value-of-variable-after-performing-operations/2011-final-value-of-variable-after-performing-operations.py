class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum1=0
        for i in operations:
            if i[0]=="-":sum1-=1
            elif i[0]=="+":sum1+=1
            else:
                if i[1]=="-":sum1-=1
                else:sum1+=1
        return sum1
        