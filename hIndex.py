class Solution:
    def hIndex(self, citations: List[int]) -> int:        
        citations.sort(reverse = True)
        count = 0
        for i , members in enumerate (citations):
            i += 1
            if i <= members:
                count += 1
        return count                
