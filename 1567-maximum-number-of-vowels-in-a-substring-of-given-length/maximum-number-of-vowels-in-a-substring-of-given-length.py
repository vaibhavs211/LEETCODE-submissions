class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        v = 0
        for i in range(k):
            if s[i] in vowels:
                v += 1
        mx_v = v
        for i in range(k,len(s)):
            if s[i] in vowels:
                v+=1
            if s[i-k] in vowels:
                v-=1
            mx_v = max(v,mx_v)
        return mx_v