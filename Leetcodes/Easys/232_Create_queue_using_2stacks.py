class MyQueue:

    def __init__(self):
        #we notice that we keep a stack of all the inputs
        #If we need to pop, then we reverse the stack by popping all the elements and
        #simultaneously pushing them to a new stack

        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)
        # print("PUSH")
        # print(self.pushStack)

    def pop(self) -> int:
        #we need to reverse the stack first
        while self.pushStack:
            val = self.pushStack.pop()
            self.popStack.append(val)
        
        # print("POP")
        # print(self.pushStack)
        # print(self.popStack)

        result = self.popStack.pop()

        #go back to the stack
        while self.popStack:
            val = self.popStack.pop()
            self.pushStack.append(val)

        # print(self.pushStack)
        # print(self.popStack)
        
        return result

    def peek(self) -> int:
        #we need to reverse the stack first
        while self.pushStack:
            val = self.pushStack.pop()
            self.popStack.append(val)
        
        top = self.popStack[-1]

        #go back to the stack
        while self.popStack:
            val = self.popStack.pop()
            self.pushStack.append(val)
        
        return top

    def empty(self) -> bool:
        # print("EMPTY")
        # print(self.pushStack)
        # print(self.popStack)
        return not (len(self.pushStack) > 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()