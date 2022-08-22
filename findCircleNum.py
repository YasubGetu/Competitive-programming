class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for province in range(len(isConnected)):
                if isConnected[city][province] and province not in visited:
                    dfs(province)
                
        visited = set()
        count = 0
        for city in range(len(isConnected)):
            if city not in visited:
                count += 1
                dfs(city)
        return count         
