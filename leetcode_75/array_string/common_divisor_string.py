class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        divisor = ''
        for i in range(1, min(len(str1), len(str2)) + 1):
            if str1[:i] == str2[:i]:
                if self.consistsOfStrings(str1, str1[:i]) and self.consistsOfStrings(str2, str1[:i]):
                    divisor = str1[:i]
        return divisor

    def consistsOfStrings(self, str1, divisor):
        if len(str1) % len(divisor) != 0:
            return False
        return divisor * int(len(str1) / len(divisor)) == str1


sol = Solution()
print(sol.gcdOfStrings('ABC', "ABCDEF"))
