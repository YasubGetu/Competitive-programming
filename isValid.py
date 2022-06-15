class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(" , "[" , "{"]
        stack = []
        for i in range(len(s)) :
            if s[i] in opening:
                stack.append(s[i])
            if stack == [] and s[i] not in opening:
                return False
            if stack != [] and s[i] not in opening:  
                if s [i] == "]" and stack[-1] != "[":
                        return False
                elif s [i] == ")" and stack[-1] != "(":
                        return False
                elif s [i] == "}" and stack[-1] != "{":
                    return False
                else:
                    stack.pop()            
        if stack == []:
            return True
        else:
            return False
        
        
