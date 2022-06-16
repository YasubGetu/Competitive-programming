class MinStack:

    def __init__(self):
        self.minStack = []
        self.minimum = []
    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.minimum == []:
            self.minimum.append(val)
        elif self.minimum[-1] >= val:
            self.minimum.append(val)
            
    def pop(self) -> None:
        if self.minStack[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.minStack.pop() 
    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
