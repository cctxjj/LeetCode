class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        columns = []
        count = 0
        for i in range(len(grid)):
            columns.append([])
            for j in range(len(grid)):
                columns[i].append(grid[j][i])
            if columns[i] in grid:
                count += grid.count(columns[i])
        return count


sol = Solution()
print(sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
