def solve(num,op):
    n2 = num.pop()
    n1 = num.pop()
    op = op.pop()
    if op == '+':
        num.append(n1+n2)
    elif op == '-':
        num.append(n1-n2)
    elif op == "*":
        num.append(n1*n2)
    else:
        num.append(n1//n2)
    
def precedence(op):
    if op == "/" or op == '*':
        return 2
    else:
        return 1

class Solution:
    def calculate(self, s: str) -> int:
        num = []
        op = []
        l = len(s)
        i = 0
        while i<l:
            if s[i] == " ":
                i+=1
                continue
            if s[i] >= '0' and s[i] <= '9':
                n = 0
                while i<l and s[i] >= '0' and s[i] <= '9':
                    n = n*10 + int(s[i])
                    i += 1
                num.append(n)
            else:
                while op and precedence(op[-1]) >= precedence(s[i]):
                    solve(num,op)
                op.append(s[i])
                i += 1
        while op:
            solve(num,op)
        return num[0]