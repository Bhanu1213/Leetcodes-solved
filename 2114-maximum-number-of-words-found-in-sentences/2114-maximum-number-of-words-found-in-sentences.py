class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1=0
        for i in sentences:
            ma=len(i.split())
            max1=max(max1,ma)
        return max1
        