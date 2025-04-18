def RLE(s):
    new_s = ""
    n = len(s)
    i = 0
    while i < n:
        curr = s[i]
        cnt = 1
        i += 1
        while i<n and s[i] == curr:
            cnt+=1
            i+=1
        new_s += str(cnt)+str(curr)
    return new_s

class Solution:
    seq = ["1"]
    def countAndSay(self, n: int) -> str:
        if n <= len(Solution.seq):
            return Solution.seq[n-1]
        result = RLE(self.countAndSay(n-1))
        Solution.seq.append(result)
        return result