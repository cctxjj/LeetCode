# put on pending
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ''
        longest_palindrome = s[0]
        for index, element in enumerate(s):
            if s.count(element) < 2:
                continue
            max_len = (len(s) - index)
            if len(longest_palindrome) > max_len:
                break
            for i in range(len(s)-1, index, -1):
                if len(s[index:i+1]) < len(longest_palindrome):
                    break
                if s[index:i+1] == self.reverse(s[index:i+1]):
                    if len(s[index:i+1]) > len(longest_palindrome):
                        longest_palindrome = s[index:i+1]
                        break

        return longest_palindrome

    def reverse(self, word):
        return word[::-1]

sol = Solution()
print(sol.longestPalindrome("aabbaa"))
