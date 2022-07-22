class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currentNumber = 0
        op = "+-*/"
        operator = "+"
        
        for i , ch in enumerate (s):
            
            if ch.isdigit():
                
                currentNumber = currentNumber * 10 + int(ch)
                
            if ch in op or i == len(s) - 1:
                
                if operator == "+":
                    
                    stack.append(currentNumber)
                    
                elif operator == "-":
                    
                    stack.append(-currentNumber)
                    
                elif operator == "*":
                    
                    stack.append(stack.pop() * currentNumber)
                    
                elif operator == "/":
                    
                    stack.append(int(stack.pop() / currentNumber))
                    
                currentNumber = 0   
                operator = ch   
            
        return sum(stack) 
