class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.get_seq(1, s)

    def get_seq(self, num, remaining_str):
        basis = ""
        next_rep = ""
        skip_bracs = 0
        for index, char in enumerate(remaining_str):
            if not char.isdigit():
                if char == "[":
                    i = int(next_rep)
                    basis += self.get_seq(i - 1, remaining_str[index + 1:])
                    next_rep = ""
                    skip_bracs += 1
                elif char == "]":
                    if skip_bracs >= 1:
                        skip_bracs -= 1
                        continue
                    else:
                        break
                else:
                    basis += char
            else:
                next_rep += char
        return basis * num



