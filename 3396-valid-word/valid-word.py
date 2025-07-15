class Solution:
    def isValid(self, word: str) -> bool:
        vow = {'a','e','i','o','u','A','E','I','O','U'}
        f1 = False
        f2 = False

        if len(word)<3:
            return False

        for ch in word:
            if not((ch>='a' and ch<='z') or (ch>='A' and ch<='Z') or (ch>='0' and ch<= '9')):
                return False

            if not f1 and ch in vow:
                f1 = True
            if not f2 and ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')) and ch not in vow:
                f2 = True
            
        return f1 and f2