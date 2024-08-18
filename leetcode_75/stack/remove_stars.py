class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            if i == len(s) - 1:
                if s[i] != "*":
                    result += s[i]

            elif s[i + 1] == "*" and s[i] == "*":
                result = result[:-1]
            elif s[i + 1] != "*" and s[i] != "*":
                result += s[i]

        return result


sol = Solution()
print(sol.removeStars("erase*****"))
