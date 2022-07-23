class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            multiplier , dig , string  = 0 , 1 , "" 
            if char != "]":
                stack.append(char)
            else:    
                while stack and char == "]" and stack[-1].isalpha():
                    string = stack.pop() + string
                stack.pop()
                while stack and stack[-1].isdigit():
                    multiplier = dig * int(stack.pop()) + multiplier
                    dig *= 10
                string *= multiplier
                stack.append(string)
        return "".join(stack)
