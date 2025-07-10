class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        res = ""
        while columnNumber:
            t = columnNumber%26
            res = s[t] + res
            if t!= 0:
                columnNumber//=26
            else:
                columnNumber = (columnNumber-1)//26
        return res