class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max1=0
        cur=0
        for i in strs:
            if i.isdigit():
                cur=int(i)
            elif i.isalnum() or i.isalpha():
                cur=len(i)
            max1=max(cur,max1)
        return max1
        