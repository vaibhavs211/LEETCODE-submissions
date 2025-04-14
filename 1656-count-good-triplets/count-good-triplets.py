class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n):
            n1 = arr[i]
            for j in range(i+1,n):
                n2 = arr[j]
                if abs(n2-n1) > a:
                    continue
                for k in range(j+1,n):
                    n3 = arr[k]
                    if abs(n3-n2) > b:
                        continue
                    if abs(n3-n1) <= c:
                        cnt += 1
        return cnt