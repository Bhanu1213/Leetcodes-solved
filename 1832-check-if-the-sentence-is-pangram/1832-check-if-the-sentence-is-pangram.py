class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        k="abcdefghikjklmnopqrstuvwxyz"
        return True if all(c in sentence for c in k) else False
        