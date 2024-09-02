class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        letters1 = {}
        for letter in word1:
            if letter not in word2:
                return False
            if letter in letters1:
                letters1[letter] += 1
            else:
                letters1[letter] = 1

        letters2 = {}
        for letter in word2:
            if letter not in word1:
                return False
            if letter in letters2:
                letters2[letter] += 1
            else:
                letters2[letter] = 1

        nums1 = sorted(letters1.values())
        nums2 = sorted(letters2.values())
        if len(nums1) != len(nums2):
            return False

        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                return False
        return True

sol = Solution()
print(sol.closeStrings('uau', 'ssx'))