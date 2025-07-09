from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # If we need all elements, just return the sorted array
        if k >= len(arr):
            return arr
            
        # Binary search to find the closest element or position
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= x:
                right = mid
            else:
                left = mid + 1
                
        # Adjust left if needed (if arr[left] is not the closest)
        if left > 0 and abs(arr[left] - x) >= abs(arr[left-1] - x):
            left -= 1
            
        # Initialize result as a deque for efficient operations from both ends
        result = deque([arr[left]])
        
        # Initialize pointers for elements to the left and right of our starting point
        left_ptr, right_ptr = left - 1, left + 1
        
        # Add k-1 more elements
        while len(result) < k:
            # If we've exhausted elements on one side, take from the other side
            if left_ptr < 0:
                result.append(arr[right_ptr])
                right_ptr += 1
            elif right_ptr >= len(arr):
                result.appendleft(arr[left_ptr])
                left_ptr -= 1
            # Compare distances and add the closer element
            elif abs(arr[left_ptr] - x) <= abs(arr[right_ptr] - x):
                result.appendleft(arr[left_ptr])
                left_ptr -= 1
            else:
                result.append(arr[right_ptr])
                right_ptr += 1
                
        return list(result)