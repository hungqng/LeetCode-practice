# 57. Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Use example from practice #56 and insert newInterval in the output
        output = []
        intervals.append(newInterval)
        for i in sorted(intervals, key = lambda i: i[0]):
            if output and i[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output += [i]
        return output

        # Solution 2
        output = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        output.append(newInterval)
        return output