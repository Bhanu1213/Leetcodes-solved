class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels={"a":-1,"e":-1,"i":-1,"o":-1,"u":-1}
        l_c=-1;count=0
        for i,char in enumerate(word):
            if char in vowels:
                vowels[char]=i
            else:
                l_c=i
            if -1 not in vowels.values():
                if min(vowels.values())>l_c:
                    count+=min(vowels.values()) - l_c
        return count
