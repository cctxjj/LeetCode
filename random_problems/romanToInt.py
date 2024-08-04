class Solution(object):

    def __init__(self):
        self.romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        prev_value = None
        for char in s:
            try:
                value = self.romans[char]
                if prev_value is not None:
                    if prev_value < value:
                        sum -= prev_value
                        sum += (value - prev_value)
                        prev_value = (value - prev_value)
                    else:
                        sum += value
                        prev_value = value
                else:
                    prev_value = value
                    sum += value
            except KeyError:
                return None
        return sum






