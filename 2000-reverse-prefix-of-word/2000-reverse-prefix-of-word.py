class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word
        else:
            k=word.index(ch)
            return word[:k+1][::-1]+word[k+1:]        