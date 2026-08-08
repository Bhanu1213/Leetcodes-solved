class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            if all(ch in allowed for ch in i):count+=1
        return count
        


        