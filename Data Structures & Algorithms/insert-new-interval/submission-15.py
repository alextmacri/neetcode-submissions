class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # For this problem there are 2 things to consider: inserting in the
        #   right place and considering any merges that need to be done. These
        #   can intuitively be done in one linear-time scan since the current
        #   intervals are already sorted and merged for us. This will give us
        #   O(n) runtime, which is intuitively the best we can do for this,
        #   since we definitely need to AT LEAST see where all the starts of
        #   the intervals are to see where to insert it, which would be O(n)
        #   since it's just a list. To ensure we can do everything in one
        #   scan, we need to keep track of where we are and the cases (insert
        #   before, merge start, merge end, or insert after?)
        new_intervals = []
        curr_i = 0

        # First, insert things before merging from before the new interval
        #   (already sorted and "merged" getting passed in)
        while curr_i < len(intervals) and intervals[curr_i][1] < newInterval[0]:
            # End of current interval LEQ start of new interval, so you can
            #   insert it normally
            new_intervals.append(intervals[curr_i])
            curr_i += 1
        
        # After this while loop, we know that the end of the current interval
        #   is GEQ the start of the new interval (this means that there could
        #   start to be some overlap with the start of the new interval).
        #   Notice that we're in the "overlap zone" from now until the end of
        #   where there could be overlap with the end of the new interval
        #   (where the start of the current interval is greater than the end
        #   of the new interval)

        # NOTE: This is kinda like "two different cases" for "two kinds of
        #   merging", but we could also just treat it as "one case" just for
        #   merging in general since we can just do the same thing either time
        #   for both since it's just one extra action (get new merged interval
        #   for both start and end instead of just one), and it also
        #   implicitly covers the "edge case" where it's just one interval we
        #   need to merge that gives us a new merged start and end, meaning
        #   we need to be able to check for both cases at once if it's the
        #   last interval for the merge start case

        # Next, traverse where there could be overlap
        while curr_i < len(intervals) and (intervals[curr_i][0] <= newInterval[0] or intervals[curr_i][0] <= newInterval[1]):
            newInterval[0] = min(intervals[curr_i][0], newInterval[0])
            newInterval[1] = max(intervals[curr_i][1], newInterval[1])
            curr_i += 1

        # Next, insert the new interval with found bounds
        new_intervals.append(newInterval)

        # Append the rest (curr_i was used and incremented as we found the
        #   interval endpoints)
        new_intervals.extend(intervals[curr_i:])

        return new_intervals