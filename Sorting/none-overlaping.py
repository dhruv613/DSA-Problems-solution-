# Python 3.9+ style - no typing import needed
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time - greedy approach
        intervals.sort(key=lambda x: x[1])
        
        # Track end of last non-overlapping interval
        prev_end = intervals[0][1]
        remove_count = 0
        
        # Check each interval starting from second
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                remove_count += 1
        
        return remove_count

print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # Output: 1