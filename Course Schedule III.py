# 630. Course Schedule III

# There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

# You will start on the 1st day and you cannot take two or more courses simultaneously.

# Return the maximum number of courses that you can take.

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap, time = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(heap, -t)
            if time > end:
                nt = heapq.heappop(heap)
                time += nt
        return len(heap)