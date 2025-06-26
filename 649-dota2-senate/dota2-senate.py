class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = d = 0
        while len(set(senate.strip())) != 1:
            new_s = ''
            for ch in senate:
                if ch == 'R':
                    if d:
                        d-=1
                        continue
                    else:
                        new_s += 'R'
                        r += 1
                else:
                    if r:
                        r-=1
                        continue
                    else:
                        new_s += 'D'
                        d += 1
            senate = new_s
        return "Radiant" if senate[0] == 'R' else 'Dire'