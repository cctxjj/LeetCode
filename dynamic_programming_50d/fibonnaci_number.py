"""
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib_series = [0, 1]
        for i in range(2, n + 1):
            fib_series.append(fib_series[i - 1] + fib_series[i - 2])
        return fib_series[n]
