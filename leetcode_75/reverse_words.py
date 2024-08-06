class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        words.reverse()
        result = ''
        for index, element in enumerate(words):
            if element != '':
                result += element + ' '
        result = result.strip()
        return result


sol = Solution()
print(sol.reverseWords("Alive Loves Bob"))
