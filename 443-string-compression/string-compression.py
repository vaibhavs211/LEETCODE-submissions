class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j = 0,0
        n = len(chars)
        while i < n:
            t = chars[i]
            cnt = 1
            i+=1
            while i < n and chars[i] == t:
                cnt+=1
                i+=1 
            chars[j] = t
            j+=1
            if cnt > 1 and cnt < 10:
                chars[j] = str(cnt)
                j += 1
            elif cnt >= 10:
                cnt = str(cnt).strip()
                for c in cnt:
                    chars[j] = c
                    j += 1
            
        return j
                
