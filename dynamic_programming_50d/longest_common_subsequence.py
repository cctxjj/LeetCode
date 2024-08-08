class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :param reverse:
        :type text1: str
        :type text2: str
        :rtype: int
        """

        longer_txt = max(text1, text2)[::]
        smaller_txt = min(text1, text2)[::]
        count = 0
        for index, letter in enumerate(longer_txt):
            if letter in smaller_txt:

                i_lower = smaller_txt.index(letter)
                curr_count = 1
                sub_seq = letter

                for checking_letter in longer_txt[index+1:]:
                    if len(sub_seq) >= len(smaller_txt):
                        return len(smaller_txt)
                    if checking_letter in smaller_txt[i_lower:]:
                        curr_count += 1
                        i_lower += smaller_txt[i_lower:].index(checking_letter) + 1
                        print(i_lower)
                        sub_seq += checking_letter

                count = max(count, curr_count)
                print(sub_seq)

        # reverse
        longer_txt = max(text1, text2)[::-1]
        smaller_txt = min(text1, text2)[::-1]
        count = 0
        for index, letter in enumerate(longer_txt):
            if letter in smaller_txt:

                i_lower = smaller_txt.index(letter)
                curr_count = 1
                sub_seq = letter

                for checking_letter in longer_txt[index + 1:]:
                    if len(sub_seq) >= len(smaller_txt):
                        return count
                    if checking_letter in smaller_txt[i_lower:]:
                        curr_count += 1
                        i_lower += smaller_txt[i_lower:].index(checking_letter) + 1
                        print(i_lower)
                        sub_seq += checking_letter

                count = max(count, curr_count)
                print(sub_seq)

        return count


sol = Solution()
print(sol.longestCommonSubsequence("xaxx", "a"))
