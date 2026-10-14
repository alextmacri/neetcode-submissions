class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # For this problem there are 2 main parts: insert the interval in the
        #   correct place, then merge any overlapping intervals. Since it's
        #   already sorted, it's not hard to see where this can be inserted in
        #   O(n) time, but for merging that could potentially happen everywhere
        #   (or nowhere) depending on the new interval bounds. We can handle
        #   these both at once (one pass, faster) by checking to see what
        #   intervals NEED to be inserted without merging (ends before the new
        #   interval starts), then doing whatever merges need to be done, then
        #   inserting the rest (starts after the new interval ends)
        new_intervals = []
        curr_i = 0
        new_interval_start = newInterval[0]
        new_interval_end = newInterval[1]

        # First, insert things before merging from before the new interval
        #   (already sorted and "merged" getting passed in)
        while curr_i < len(intervals) and intervals[curr_i][1] < newInterval[0]:
            # End of current interval LEQ start of new interval, so you can
            #   insert it normally
            new_intervals.append(intervals[curr_i])
            curr_i += 1

        # Next, find the start of the new interval (what merges at start?)
        while curr_i < len(intervals) and intervals[curr_i][0] <= newInterval[0]:
            # End of current interval greater than start of new interval and
            #   start of current interval LEQ start of new interval, so you
            #   merge start
            new_interval_start = intervals[curr_i][0]
            new_interval_end = max(intervals[curr_i][1], new_interval_end)
            curr_i += 1

        # Next, find the end of the new interval (what merges at end?)
        while curr_i < len(intervals) and intervals[curr_i][0] <= newInterval[1]:
            # Start of current interval greater than start of new interval and
            #   start of current interval less than end of new interval, so
            #   you merge end if necessary
            new_interval_end = max(intervals[curr_i][1], new_interval_end)
            curr_i += 1

        # Next, insert the new interval with found bounds
        new_intervals.append([new_interval_start, new_interval_end])

        # Append the rest (curr_i was used and incremented as we found the
        #   interval endpoints)
        new_intervals.extend(intervals[curr_i:])

        return new_intervals