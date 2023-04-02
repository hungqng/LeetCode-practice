# 1029. Two City Scheduling

# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0] - x[1])
        
        N = len(costs)
        half = N // 2
        
        min_sum = sum([a for a, b in costs[:half]]) + sum([b for a, b in costs[half:]])
        
        return min_sum

        # Solution 2        
        # refund = []
        # N = len(costs)//2
        # minCost = 0
        # for A, B in costs:
        #     refund.append(B - A)
        #     minCost += A
        # refund.sort()
        # for i in range(N):
        #     minCost += refund[i]
        # return minCost
