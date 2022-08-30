class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        stack = []
        for i in range (len(points)):
            if not stack or stack[-1][1] < points[i][0]:
                stack.append(points[i])
                continue
            if stack[-1][1] > points[i][1]:
                stack.pop()
                stack.append(points[i])
            else:
                a = stack.pop()
                stack.append([points[i][0] , a[1]])  
        return len(stack)        
            
