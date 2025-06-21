class StockSpanner:

    def __init__(self):
        #Monotonically DECREASING stack
        self.stack = deque()

    def next(self, price: int) -> int:
        cur_span = 1
        while self.stack:
            val, span = self.stack[-1]
            if val <= price:
                self.stack.pop()
                cur_span += span
            else:
                break

        self.stack.append((price, cur_span))
        return cur_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)