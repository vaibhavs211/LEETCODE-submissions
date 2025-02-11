class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l = len(part)
        while part in s:
            i = s.find(part) 
            s = s[:i] + s[i + l:] 
        return s