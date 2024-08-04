"""
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
"""


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        trib_series = [0, 1, 1]
        for i in range(3, n + 1):
            trib_series.append(trib_series[i - 1] + trib_series[i - 2] + trib_series[i - 3])
        return trib_series[n]
