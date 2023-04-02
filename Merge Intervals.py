# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 0(nlogn)
        intervals.sort(key = lambda i : i[0]) # sort intervals by index of 0
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

        # Solution 2
        output = []
        for i in sorted(intervals, key = lambda i: i[0]):
            if output and i[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output += [i]
        return output