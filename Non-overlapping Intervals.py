# 435. Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])

        # Initialize variables
        count = 1  # Count of non-overlapping intervals (at least 1, since we pick the one with the earliest end time)
        end_time = intervals[0][1]

        # Greedily select non-overlapping intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time:
                count += 1
                end_time = intervals[i][1]

        return len(intervals) - count