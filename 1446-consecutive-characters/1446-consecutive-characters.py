class Solution:
    def maxPower(self, s: str) -> int:
        max_count=0
        cur_count=0
        char=""
        for i in s:
            if i!=char:
                char=i
                cur_count=1
            elif i==char:cur_count+=1
            if cur_count>max_count:max_count=cur_count
        return max_count