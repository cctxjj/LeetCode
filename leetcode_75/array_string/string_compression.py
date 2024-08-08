class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0:
            return 0
        if len(chars) == 1:
            return 1
        last_char = chars[0]
        result = ""

        count_cons_chars = 1
        for index, char in enumerate(chars[1:]):

            if char == last_char:
                count_cons_chars += 1
                if index+1 == len(chars)-1:
                    result += chars[index]
                    result += str(count_cons_chars)
            else:
                result += last_char
                if count_cons_chars > 1:
                    result += str(count_cons_chars)
                count_cons_chars = 1
                if index+1 == len(chars)-1:
                    result += chars[index+1]
            last_char = char

        chars[0:len(result)] = result
        print(chars)
        return len(result)


sol = Solution()
print(sol.compress(["a","b","c"]))
