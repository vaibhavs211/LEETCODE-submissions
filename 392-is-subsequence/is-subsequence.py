class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        m = len(s)
        if m==0:
            return True
        for ch in t:
            if ch == s[i]:
                i+=1
            if i == m:
                return True
        return False