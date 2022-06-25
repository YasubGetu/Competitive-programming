class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = []
        while start < end:
            area.append(min(height[start] , height[end]) * (end - start))
            if height[start] > height[end]:
                end -= 1
            elif height[start] <= height[end]:
                start += 1
        return max(area)
