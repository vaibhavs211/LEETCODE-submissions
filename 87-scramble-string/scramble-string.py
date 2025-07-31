class Solution:
    def __init__(self):
        self.mp = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        if s1 == s2:
            return True
        if len(s1) == 1:
            return False
        key = s1 + " " + s2
        if key in self.mp:
            return self.mp[key]
        n = len(s1)
        
        for i in range(1,n):
            wo = self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])
            if wo:
                self.mp.update({key:True})
                return True
            
            wi = self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i])
            if wi:
                self.mp.update({key:True})
                return True
        
        self.mp.update({key:False})
        return False
    
