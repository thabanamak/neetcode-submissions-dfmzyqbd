class MinStack:

    def __init__(self):
        self.stack = []
        self.small_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.small_stack or val <= self.small_stack[-1]:
            self.small_stack.append(val)
        

    def pop(self) -> None:
        removed_val = self.stack.pop()
        if removed_val == self.small_stack[-1]:
            self.small_stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.small_stack[-1]

        
