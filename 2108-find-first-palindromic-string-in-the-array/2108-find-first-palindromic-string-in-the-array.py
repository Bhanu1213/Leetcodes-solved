class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pa=""
        for i in words:
            if i==i[::-1]:
                return i
        return pa
        