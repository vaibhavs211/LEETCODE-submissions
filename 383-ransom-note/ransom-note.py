from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)

        for key in a.keys():
            if key not in b or a[key]>b[key]:
                return False
        return True