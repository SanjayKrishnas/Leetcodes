class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Use a regular list instead of deque for stack operations
        stack = []  # [height, index]
        result = 0
        
        for i in range(len(heights)):
            start = i
            
            # Pop the stack and calculate area when we find a smaller height
            while stack and stack[-1][0] > heights[i]:
                h, pos = stack.pop()
                result = max(result, h * (i - pos))
                start = pos  # Update start position
            
            # Push current height with its leftmost valid position
            stack.append([heights[i], start])
        
        # Process remaining elements in the stack
        for h, pos in stack:
            result = max(result, h * (len(heights) - pos))
        
        return result