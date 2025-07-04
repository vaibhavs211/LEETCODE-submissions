class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ob = 0
        res = ""
        for ch in s:
            if not stack and ch == '(':
                stack.append(ch)
            elif ch == '(':
                ob += 1
                res += ch
            elif ob and ch == ')':
                ob-=1
                res += ch
            else:
                stack.pop()
        return res