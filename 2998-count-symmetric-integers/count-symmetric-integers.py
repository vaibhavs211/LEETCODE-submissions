class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low, high+1):
            n = str(i)
            x = len(n)
            if x%2 != 0:
                continue
            else:
                fh = n[:(x//2)]
                sh = n[(x//2):]

                if sum([int(k) for k in fh]) == sum([int(l) for l in sh]):
                    c += 1
        return c

