class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split();arr=[""]*len(words)
        for i in words:
            arr[int(i[-1])-1]=i[:-1]
        return " ".join(arr)

        