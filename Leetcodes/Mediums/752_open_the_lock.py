from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1

        visited = set()
        queue = deque()
        queue.append("0000")
        visited.add("0000")

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                num = queue.popleft()

                if num == target:
                    return level

                if num in dead_set:
                    continue

                for i in range(4):
                    digit = int(num[i])
                    for move in [-1, 1]:
                        new_digit = (digit + move) % 10
                        new_combo = num[:i] + str(new_digit) + num[i+1:]
                        if new_combo not in visited and new_combo not in dead_set:
                            visited.add(new_combo)
                            queue.append(new_combo)
            level += 1

        return -1
