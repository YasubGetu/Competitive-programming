class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        for i in range (len(popped) - 1):
            x = pushed.index(popped[i])
            pushed.pop(x)
            if pushed.index(popped[i + 1]) != x - 1 and pushed.index(popped[i + 1]) < x :
                return False
        return True   
