# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        curlevel = deque()
        curlevel.append(root)
        result = []

        while curlevel:
            level_size = len(curlevel)
            current_level_values = []  # Temporary list to store values of the current level

            for _ in range(level_size):
                node = curlevel.popleft()
                current_level_values.append(node.val)  # Append the value of the current node

                if node.left:
                    curlevel.append(node.left)
                if node.right:
                    curlevel.append(node.right)

            result.append(current_level_values)  # Add current level values to the result

        return result
