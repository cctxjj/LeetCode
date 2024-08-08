class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        i = 0
        while i < min(len(word1), len(word2)):
            result += word1[i] + word2[i]
            i += 1
        if len(word1) > i:
            result += word1[i:]
        elif len(word2) > i:
            result += word2[i:]
        return result

sol = Solution()
print(sol.mergeAlternately('abcefgh', 'abcdfghij'))