class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minstack = deque()

    def push(self, val: int) -> None:
        #we push the val onto the stack
        self.stack.append(val)
        #then we push the minimum of the current stack top and the current val onto the stack
        if self.minstack:
            min_stack_top = self.minstack[-1]
            minim = min(min_stack_top, val)
            self.minstack.append(minim)
        else: #stack is empty
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()