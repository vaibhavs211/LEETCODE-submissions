class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i=j=0
        if len(s)!= len(goal):
            return False
        n = len(s)
        temp = 0
        while True:
            j = temp
            i = 0
            while j<n and s[i] != goal[j]:
                j += 1
            if j == n:
                return False
            temp = j+1
            while i<n and s[i] == goal[j]:
                i += 1
                j = (j+1)%n
            if i == n:
                return True
            