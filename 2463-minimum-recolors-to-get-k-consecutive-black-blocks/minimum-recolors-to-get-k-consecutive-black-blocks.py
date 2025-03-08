class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        w_cnt = blocks[0:k].count("W")
        result = 100
        n =len(blocks)
        while i + k <= n:
            result = min(result,w_cnt)
            if blocks[i] == 'W':
                w_cnt -= 1
            if i+k < n and blocks[i+k] == 'W':
                w_cnt += 1
            i+=1 
        return result