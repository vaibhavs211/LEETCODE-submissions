import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = [[-(x+1)/(y+1) + x/y, x, y] for x,y in classes]
        heapq.heapify(n)
        for _ in range(extraStudents):
            t = heapq.heappop(n)
            t[1] += 1
            t[2] += 1
            t[0] = -((t[1]+1) / (t[2] + 1)) + t[1]/t[2]
            heapq.heappush(n,t)
        
        s = 0
        for _,x,y in n:
            s += x/y
        
        return s/len(n)