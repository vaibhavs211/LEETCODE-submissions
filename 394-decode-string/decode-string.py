class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        n = len(s)
        l = []
        while i<n:
            if s[i]>= '0' and s[i] <= '9':
                new = ""
                while i<n and s[i]>= '0' and s[i] <= '9':
                    new += s[i]
                    i+=1
                l.append(int(new))
            elif s[i] == '[':
                l.append('[')
                i+=1
            elif s[i] >= 'a' and s[i] <= 'z':
                new = ""
                while i<n and s[i] >= 'a' and s[i] <= 'z':
                    new += s[i]
                    i+=1
                l.append(new)
            else:
                l.append(']')
                i+=1
        n = len(l)
        res = ""
        stack = []
        for e in l:
            if e == ']':
                t1 = ""
                while stack[-1]!='[':
                    t1 = stack.pop() + t1
                stack.pop()
                t2 = stack.pop()
                t3 = ""
                if stack and stack[-1] != '[':
                    t3 = stack.pop()
                stack.append(t3+(t1*t2))
            else:
                stack.append(e)
        return "".join(stack)