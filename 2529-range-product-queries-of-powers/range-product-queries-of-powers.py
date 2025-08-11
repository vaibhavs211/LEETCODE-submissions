def ps(a):
    res = [1]
    for i in range(len(a)):
        res.append(res[i] * a[i])
    return res

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        a = []
        x = 1
        res = []
        num = (bin(n)[2:])[::-1]
        for ch in num:
            if ch == '1':
                a.append(x)
            x <<= 1
        
        MOD = 10**9 + 7
        pref = ps(a)
        # return pref
        for q in queries:
            res.append((pref[q[1]+1] // pref[q[0]])%MOD)
        
        return res