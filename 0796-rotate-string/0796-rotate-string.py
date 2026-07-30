class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal)!=len(s):return False
        s2=s+s
        if goal in s2: return True
        else: return False 
        