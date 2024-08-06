class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        in_word = []
        for word in wordDict:
            if word in s:
                in_word.append(word)

        if len(in_word) == 0:
            return False

        in_word.sort()

        curr_split_word = ''
        curr_split = []
        for index_l, letter in enumerate(s):
            curr_split_word += letter
            for index_w, word in enumerate(in_word):
                if curr_split_word == word:
                    if index_w == len(in_word)-1 or index_l == len(s)-1:
                        curr_split.append(word)
                        curr_split_word = ''
                        continue
                    elif curr_split_word + s[index_l+1] != in_word[index_w+1]:
                        curr_split.append(word)
                        curr_split_word = ''

        return ''.join(curr_split) == s



sol = Solution()
print(sol.wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaa"]))
