class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        pairs = {}
        for index, element in enumerate(nums):
            if element in pairs:
                continue
            missing_nums = self.twoSum(nums=nums, target=-1*element, skip_ind=index)
            if missing_nums is not False:
                for res in missing_nums:
                    solution = [element, nums[res[0]], nums[res[1]]]
                    solution.sort()
                    pairs[solution[0]] = (solution[1], solution[2])
                    if solution in result:
                        print("skipped 2")
                        continue
                    result.append(solution)

        return result

    def twoSum(self, nums, target, skip_ind=None):
        pairs = {}
        results = []
        for index, number in enumerate(nums):
            if skip_ind is not None:
                if index == skip_ind:
                    continue
            if number in pairs:
                results.append((pairs[number], index))
            else:
                pairs[target-number] = index
        if len(results) == 0:
            return False
        else:
            return results



