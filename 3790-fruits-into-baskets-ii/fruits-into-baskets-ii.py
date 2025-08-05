class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        visited = set()
        ans = 0
        for n in fruits:
            f = True
            for i in range(len(baskets)):
                if i not in visited and baskets[i] >= n:
                    visited.add(i)
                    f = False
                    break
            if f:
                ans+=1
        return ans