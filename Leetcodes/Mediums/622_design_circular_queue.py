class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.cur_size = 0

        self.head = None #keep track of the front of our queue
        self.tail = None #keep track of the end of our queue

    def enQueue(self, value: int) -> bool:
        #1. capacity is met already
        if self.cur_size == self.max_size: return False
        #2. queue is empty
        if self.head == None and self.tail == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        #3. else we add normally to the tail end of our queue
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.cur_size += 1
        return True

    def deQueue(self) -> bool:
        #1. queue is empty
        if self.isEmpty(): return False
        #2. remove head element from the queue
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        self.cur_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1

        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        if self.cur_size == 0: return True
        return False

    def isFull(self) -> bool:
        if self.cur_size == self.max_size: return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()