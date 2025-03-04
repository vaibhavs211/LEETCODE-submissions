class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0
        powers = []
        while 3**i <= 10000000:
            powers.append(3**i)
            i+=1
        
        i = len(powers) - 1
        while i >= 0:
            if n>=powers[i]:
                n-=powers[i]
            i-=1
        return True if n == 0 else False