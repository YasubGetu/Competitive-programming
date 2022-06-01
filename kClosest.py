class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda point: pow(point[1] , 2) + pow(point[0] , 2))
        return points[:k]
