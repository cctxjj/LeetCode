class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        num_vowels = 0
        num_max_vowels = 0
        start_window = 0
        for end_window in range(len(s)):
            if s[end_window] in vowels:
                num_vowels += 1
            if (end_window - start_window + 1) == k:
                num_max_vowels = max(num_max_vowels, num_vowels)
                if s[start_window] in vowels:
                    num_vowels -= 1
                start_window += 1
        return num_max_vowels

sol = Solution()
print(sol.maxVowels("abcdiiisuvh", 3))
