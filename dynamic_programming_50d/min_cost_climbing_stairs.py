# indian told me to start from the top and move downward assigning each step a minimum cost to reach it from the top

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        min_cost = []
        for element in cost:
            min_cost.append(element)
        min_cost.append(0)
        for i in range(len(cost)-2, -1, -1):
            min_cost[i] = cost[i]+min(min_cost[i+1], min_cost[i+2])
        return min(min_cost[0], min_cost[1])

