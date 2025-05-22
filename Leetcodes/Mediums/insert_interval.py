class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update newInterval to cover the entire overlapping range
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged interval
        result.append(newInterval)
        
        # Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
            

