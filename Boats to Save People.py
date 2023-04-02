# 881. Boats to Save People

# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        start, end = 0, len(people) -1
        counter = 0
        people.sort()
        
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            counter += 1
            end -= 1
        return counter

        #Solution 2
        # people.sort(reverse=True)
        # i, j = 0, len(people) - 1
        # while i <= j:
        #     if people[i] + people[j] <= limit: j -= 1
        #     i += 1
        # return i