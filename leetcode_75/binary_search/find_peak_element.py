class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        index = int(round(len(nums) / 2))
        cont = True
        while cont and 0 <= index <= len(nums)-1:
            if index - 1 >= 0 and nums[index - 1] > nums[index]:
                index -= 1
                continue
            elif index + 1 <= len(nums)-1 and nums[index + 1] > nums[index]:
                index += 1
                continue
            else:
                cont = False

        return index

sol = Solution()
print(sol.findPeakElement([0]))
