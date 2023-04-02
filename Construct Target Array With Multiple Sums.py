# 1354. Construct Target Array With Multiple Sums

# You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < n and set the value of arr at index i to x.
# You may repeat this procedure as many times as needed.
# Return true if it is possible to construct the target array from arr, otherwise, return false.

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-a for a in target]
        heapq.heapify(target)
        while True:
            a = -heapq.heappop(target)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(target, -a)

        # Solution 2
        if len(target) == sum(target): return True
        if len(target) == 1: return False
        h = [-n for n in target]
        total = sum(target)
        heapify(h)
        while total != len(target):
            # print(h)
            cand = -heappop(h)
            rest = total - cand
            new = cand - rest
            if new <=0: return False
            if new > rest:
                new = new%rest + rest
            heappush(h,-new)
            total = new + rest
        return True

        # Solution 3
        heap = [-num for num in target]
        total = sum(target)
        heapify(heap)
        while heap[0] != -1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1: return False
            num %= total
            total += num
            heappush(heap, -num or -total)
        return True