class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for word in text.split():
            for letter in brokenLetters:
                if letter in word:
                    break
            else:
                res += 1
        
        return res