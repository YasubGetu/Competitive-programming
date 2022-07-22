class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [2,4]
        for i in range(len(num)):
            while stack and k and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        stack = stack [: len(stack) - k]
        if stack == [] :
            return "0"
        else:
            return str(int("".join(stack)))        
