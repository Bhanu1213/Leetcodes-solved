class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub=" ".join(i.lower() for i in s if i.isalnum())
        return sub==sub[::-1] 