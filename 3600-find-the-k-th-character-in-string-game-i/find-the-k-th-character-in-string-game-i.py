word = ['a']
class Solution:
    def kthCharacter(self, k: int) -> str:
        if len(word[0]) >= k:
            return word[0][k-1]
        while len(word[0])<k:
            t = word[0]
            for ch in t:
                word[0] += 'a' if ch=='z' else chr(ord(ch)+1)
        return word[0][k-1] 