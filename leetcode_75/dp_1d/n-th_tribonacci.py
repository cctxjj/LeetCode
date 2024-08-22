class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [0, 1, 1]
        for i in range(3, n+1):
            t.append(t[i - 1] + t[i - 2] + t[i - 3])
        return t[n]
