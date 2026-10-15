class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Intuitively, there are simple ways to do this in one O(n) scan
        #   once the input array is sorted, which it doesn't say if it is
        #   (meaning it's safe to assume it may not be for any given input).
        #   So, once the input array is sorted, we know that the lowest of any
        #   merge is the start of the first interval. So, we could just
        #   iterate along and keep track of the current lowest and highest,
        #   and whenever there's a gap between new low and current high, we
        #   start a new interval. We can use Python's built-in sort to do a
        #   sort in-place (assuming it uses quicksort), and we can do the
        #   scan in place with O(1) auxilliary variables for keeping traack of
        #   current lows and highs for merges

        # Edge case: intervals is empty
        if intervals == []:
            return []

        # First, sort by the start of the intervals to ensure that the
        #   invariant described above holds true (lowest of all merged
        #   intervals is the low end of the first one)
        intervals.sort(key=lambda x: x[0])

        # Now that it's sorted, we can iterate through with the strategy
        #   described above
        # NOTE: we are using a while loop with a dynamic curr_i that we
        #   can control so we can have an easier time doing this in place
        #   (editing and removing elements from the list as we go, which isn't
        #   as clean with a typical Python for/foreach loop)
        curr_i = 0
        while curr_i < len(intervals) - 1:
            if intervals[curr_i][1] >= intervals[curr_i + 1][0]:
                # Current ends after next's start => merge. This means we have
                #   to ensure the merge has the largest of the two ends (we
                #   know it has the smallest of the two starts due to the
                #   sorted start loop invariant), then remove the merged
                #   interval from the list
                intervals[curr_i][1] = max(intervals[curr_i][1], intervals[curr_i + 1][1])
                intervals.pop(curr_i + 1)
            else:
                # Current ends before next's start => no merge. This means
                #   just move on to the next
                # NOTE: due to sorted start invariant we guarunteed, this will
                #   always work to see if it merges with anything beyond
                curr_i += 1
        
        return intervals