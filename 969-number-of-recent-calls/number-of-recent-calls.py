class RecentCounter:
    
    def __init__(self):
        self.l = []
        self.c = 0

    def ping(self, t: int) -> int:
        self.l.append(t)
        self.c += 1
        i = 0
        while self.l[i] < t-3000:
            i += 1
            self.c -= 1
        self.l = self.l[i::]
        return self.c


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)