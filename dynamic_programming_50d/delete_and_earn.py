
# This is shit

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_count = 0
        biggest = 0

        for i in range(len(nums)):
            curr_count = 0

            nums_copy = nums.copy()

            while len(nums_copy) > 0:
                curr_count += self.__earn__(nums_copy, index=i)
            biggest = max(biggest, curr_count)
        return biggest

    def __earn__(self, nums, index):
        base_number = nums.pop(index)

        if index >= len(nums)-1:
            upper_target = None

            for i in range(index, len(nums)):
                if upper_target is None:
                    if nums[i] != base_number:
                        upper_target = nums[i]
                        while nums[i] == upper_target:
                            nums.pop(i)
                            if len(nums) - 1 < i:
                                break
                        break
        if index > 0:

            lower_target = None

            for i in range(index, -1, -1):
                if lower_target is None:
                    if nums[i] != base_number:
                        lower_target = nums[i]
                        count = 0
                        while nums[i - count] == lower_target:
                            nums.pop(i - count)
                            count += 1
                        break

        return base_number

sol = Solution()
sol.deleteAndEarn([3, 4, 2])
