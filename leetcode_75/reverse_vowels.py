class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_in_s = []
        indexes_in_s = []
        for index, char in enumerate(s):
            if char.lower() in vowels:
                vowels_in_s.append(char)
                indexes_in_s.append(index)
        val = list(s)
        vowels_in_s.reverse()
        for i in range(0, len(indexes_in_s)):
            val[indexes_in_s[i]] = vowels_in_s[i]

        return "".join(val)


sol = Solution()
print(sol.reverseVowels("aA"))
