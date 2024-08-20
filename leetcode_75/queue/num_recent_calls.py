class RecentCounter(object):

    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        last_pings = []
        for p in self.pings[::-1]:
            if t - 3000 <= p:
                last_pings.append(p)
            else:
                return len(last_pings)
        return len(last_pings)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
