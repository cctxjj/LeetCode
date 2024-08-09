class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str --> subsequence
        :type t: str --> original string
        :rtype: bool
        """
        if s == "" or s is None:
            return True

        curr_subsequence = 0
        for i in range(len(t)):
            if t[i] == s[curr_subsequence]:
                curr_subsequence += 1
                if curr_subsequence == len(s):
                    return True
        return False


