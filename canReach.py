class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = [start]
        visited = set()
        visited.add(start)
        while queue:
            curr = queue.pop(0)
            a = curr + arr[curr]
            b = curr - arr[curr]
            if arr[curr] == 0:
                return True
            if a >= 0 and a < n:
                if a not in visited:
                    visited.add(a)
                    queue.append(a)
                if arr[a] == 0:
                    return True
            if b >= 0 and b < n:
                if b not in visited:
                    visited.add(b)
                    queue.append(b)
                if arr[b] == 0:
                    return True
        return False  
