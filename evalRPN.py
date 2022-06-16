class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+" , "-" , "*"  , "/"]
        for i in range (len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                y= stack.pop()
                x = stack.pop()
                if tokens[i] == "/":
                    if x/y <0:
                        stack.append(-int(abs(x/y)))
                    else:
                        stack.append(x//y)                     
                elif tokens[i] == "*":
                    stack.append(x*y)    
                elif tokens[i] == "+":
                    stack.append(x+y)    
                elif tokens[i] == "-":
                    stack.append(x-y)
            # print(stack)       
        return stack.pop()            
