class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # changer = set (intervals)
        # interval = list(changer)
        nonOverlapping = []
        intervals.sort(key = lambda point : point[0])
        for i in range(len(intervals)):
            if nonOverlapping == [] or intervals [i][0] > nonOverlapping[-1][1]:
                nonOverlapping.append(intervals[i])
            else:
                nonOverlapping[-1] = [nonOverlapping[-1][0],max(intervals[i][1] , nonOverlapping[-1][1])]
        return nonOverlapping        
