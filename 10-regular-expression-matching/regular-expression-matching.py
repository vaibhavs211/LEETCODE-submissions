from functools import lru_cache
class Solution:
    def isMatch(self, a: str, b: str) -> bool:
        @lru_cache(None)
        def helper(a,b,i,j):
            if i == len(a):
                if j == len(b) or (j == len(b)-1 and b[j] == '*'):
                    return True
                else:
                    while j+1< len(b) and b[j+1] == '*':
                        j += 2
                    return j == len(b)
            if j == len(b):
                return False
            
            if j + 1 < len(b) and b[j + 1] == '*':
                if a[i] == b[j] or b[j] == '.':
                    return helper(a, b, i + 1, j) or helper(a, b, i, j + 2)
                else:
                    return helper(a, b, i, j + 2)

            if a[i] == b[j] or b[j] == '.':
                return helper(a,b,i+1,j+1)
            
            # if b[j] == '*':
            #     if a[i] == b[j-1] or b[j-1] == '.':
            #         return helper(a,b,i+1,j) or helper(a,b,i,j+1)
            #     else:
            #         return helper(a,b,i,j+1)
            

            if a[i] != b[j] and j<len(b)-1 and b[j+1] != '*':
                return False
            elif a[i] != b[j]:
                return helper(a,b,i,j+1)
        return helper(a,b,0,0)