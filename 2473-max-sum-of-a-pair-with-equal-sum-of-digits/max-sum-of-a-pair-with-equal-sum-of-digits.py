class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digSum = [(num,sum(int(x) for x in str(num))) for num in nums]
        digSum.sort(key=lambda x: x[1])
        n = len(digSum)
        i = 0
        res = -1
        while i<n-1:
            if digSum[i][1] == digSum[i+1][1]:
                sm = digSum[i][1]
                mx1 = digSum[i][0]
                mx2 = 0
                i+=1
                while i<n and digSum[i][1] == sm:
                    if digSum[i][0] > mx1:
                        mx2 = mx1
                        mx1 = digSum[i][0]
                    elif digSum[i][0] > mx2:
                        mx2 = digSum[i][0]
                    i+=1
                res = max(res,mx1+mx2)
                i-=1
            i+=1
        return res
            