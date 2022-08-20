"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        answer = []
        
        for x in range (1 , 1001):
            start , end = 1 , 1000
            
            while start <= end:
                mid = start + (end - start)//2                
                solution = customfunction.f(x , mid)
                
                if solution == z:                    
                    answer.append([x , mid])
                    curr = mid + 1
                    
                    while customfunction.f(x , curr) == z:
                        answer.append([x , curr])
                        curr += 1
                    curr = mid - 1
                    while customfunction.f(x , curr) == z:
                        answer.append([x , curr])
                        curr -= 1
                
                    break
                    
                elif solution < z:
                    start = mid + 1
                elif solution > z:
                    end = mid - 1
                    
        return answer             
                        
                
        
