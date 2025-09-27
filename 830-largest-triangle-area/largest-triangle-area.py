import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    x1,x2,x3 = points[i][0], points[j][0], points[k][0]
                    y1,y2,y3 = points[i][1], points[j][1], points[k][1]
                    res = max(res, abs(0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))))
        return res