class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        i = 0
        if n == 1:
            return strs[0]
        try:
            while i<(len(strs[0])):
                for j in range(1,n):
                    if strs[j][i] != strs[0][i]:
                        return strs[0][:i]
                i+=1
        except Exception:
            return strs[0][:i]
        return strs[0][:i]