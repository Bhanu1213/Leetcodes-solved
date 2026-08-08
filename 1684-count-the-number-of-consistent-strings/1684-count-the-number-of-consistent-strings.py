class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        # for i in words:
        #     if all(ch in allowed for ch in i):count+=1
        # return count
        allowed=set(allowed)
        count=0
        for i in words:
            for j in i:
                if j not in allowed:
                    count+=1
                    break
        return len(words)-count

        


        