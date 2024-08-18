class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # prechecks to avoid useless looping
        if len(word1) != len(word2):
            return False
        if word1 == word2:
            return True

        chars_words1 = {}
        close_word = word1
        for index, char in enumerate(word1):
            if char != word2[index]:
                if word2 in chars_words1:
                    pass
#!to be finished

