class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        curr = '/'
        for i in range(len(num)-2):
            if num[i] > curr and num[i] == num[i+1] == num[i+2]:
                res = num[i] * 3
                curr = num[i]
            
        return res
