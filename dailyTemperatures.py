class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        lastIndex = 0
        for i , t in enumerate (temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                stackT , stackI = stack.pop()
                output[stackI] = i - stackI
            stack.append([t , i])  
        return output            
