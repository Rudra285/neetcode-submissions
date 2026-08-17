class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: (i[0], i[1]))
        merged_intervals = []
        merged = []

        if len(intervals) <= 1:
            return intervals

        for i in range(1, len(intervals)):
            if merged:
                if intervals[i][0] <= merged[1]:
                    start = min(intervals[i][0], merged[0])
                    end = max(intervals[i][1], merged[1])
                    merged = [start, end]
                else:
                    merged_intervals.append(merged)
                    merged = [intervals[i][0], intervals[i][1]]
            else:
                if intervals[i][0] <= intervals[i - 1][1]:
                    start = min(intervals[i][0], intervals[i - 1][0])
                    end = max(intervals[i][1], intervals[i - 1][1])
                    merged = [start, end]
                else:
                    merged_intervals.append([intervals[i - 1][0], intervals[i - 1][1]])
                    merged = [intervals[i][0], intervals[i][1]]
                
        merged_intervals.append(merged)
        
        return merged_intervals