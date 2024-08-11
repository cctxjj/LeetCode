class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        a = 0
        b = len(nums) - 1

        operations = 0

        while a < b:
            if nums[a] + nums[b] == k:
                operations += 1
                a += 1
                b -= 1
            elif nums[a] + nums[b] > k:
                b -= 1
            elif nums[a] + nums[b] < k:
                a += 1
        return operations


sol = Solution()
print(sol.maxOperations([1, 2, 3, 4], k=5))
