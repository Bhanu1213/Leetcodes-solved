class Solution:
    def maxDistinct(self, s: str) -> int:
        se=set()
        count=0
        for i in s:
            if i not in se:
                count+=1
            se.add(i)
        return count
