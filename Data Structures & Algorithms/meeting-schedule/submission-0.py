"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # First, we must sort the intervals to make them easier to compare,
        #   since they may be provided in any order
        intervals.sort(key=lambda x: x.start)

        # Now, we iterate through and check to see if there are any instances
        #   of overlap between previous endings and next beginnings
        return not any(intervals[i].end > intervals[i + 1].start for i in range(len(intervals) - 1))