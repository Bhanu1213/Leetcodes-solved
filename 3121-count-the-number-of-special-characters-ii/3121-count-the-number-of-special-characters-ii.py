class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        ig=set()
        for i in range(len(word)-1,-1,-1):
            if word[i].islower():
                ig.add(word[i])
                continue
            else:
                if word[i].lower() in ig:
                    continue
                else:
                    if word[i].lower() in word[:i] and word[i] not in word[:i-1]:
                        if word[i] not in ig:
                            count+=1
                            ig.add(word[i])
        return count

        