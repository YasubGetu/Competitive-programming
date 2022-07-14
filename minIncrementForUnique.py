class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        count = 0 
        unique = []
        
        for i in nums:
            if not unique or i > unique[-1]:
                unique.append(i)
            else:
                diff = 1 + unique[-1] - i
                count += diff
                unique.append(i + diff)
        return count        
