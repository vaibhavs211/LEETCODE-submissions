class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        res = [a[0]]
        for i in range(1,len(a)):
            if res and ((res[-1] > 0 and a[i] > 0) or (res[-1] <0 and a[i] < 0)):
                res.append(a[i])
            elif not res:
                res.append(a[i])
            else:
                if a[i]<0 and (abs(res[-1]) > abs(a[i])):
                    continue
                else:
                    if a[i] < 0:
                        f = True
                        while res and res[-1] > 0:
                            if (-1)*res[-1] < a[i]:
                                break
                            elif (-1)*res[-1] > a[i]:
                                res.pop()
                            else:
                                res.pop()
                                f = False
                                break
                        if f and (not res or res[-1] < 0):
                            res.append(a[i])
                    else:
                        res.append(a[i])
        return res