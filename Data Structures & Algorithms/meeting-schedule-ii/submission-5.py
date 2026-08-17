"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        
        intervals.sort(key=lambda x: (x.start, x.end))
        j = 1
        occupied = []

        for interval in intervals:
            if occupied and interval.start >= occupied[0][0]:
                heapq.heappop(occupied)
            heapq.heappush(occupied, (interval.end, interval.start))
        return len(occupied)
