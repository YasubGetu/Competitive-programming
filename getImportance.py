"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = {emp.id : emp for emp in employees}
        def dfs(key):
            currEmployee = employee[key].importance
            for sub in employee[key].subordinates:
                currEmployee += dfs(sub)
            return currEmployee  
        return dfs(id)
        
