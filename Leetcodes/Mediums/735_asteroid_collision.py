from collections import deque
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        stack = deque()

        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            if ast < 0: #so now we have to check for collisions
                if stack:
                    while stack:
                        pos_ast = stack[-1]
                        if pos_ast == abs(ast): #pop and stop checking
                            stack.pop()
                            break
                        elif pos_ast < abs(ast): #pop and continue checking
                            stack.pop()

                            #if we pop and have to continue checking but stack is EMPTY
                            #then we add asteroid to result
                            if not stack:
                                result.append(ast)
                        elif pos_ast > abs(ast): #stop checking
                            break

                else: #stack is empty
                    result.append(ast) #simply append the neg asteroid
        
        if stack: #EXTEND remaining postive asteroids if it exists (append it to the end)
            result.extend(stack)

        return result