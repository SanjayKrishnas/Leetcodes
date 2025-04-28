# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #at each node we can combine the max left + center + max right to get the valuee of the current node
        #we return the max path (either left or right along with center)
        #or we return 0 if the max path is negative

        result = -1000
        def findMax(root):
            nonlocal result
            if root == None:
                return 0

            cur_val = root.val
            left = findMax(root.left)
            right = findMax(root.right)

            cur_max = max(cur_val + left + right, cur_val + left, cur_val + right, cur_val) #or just the node itself

            if cur_max > result: result = cur_max
            return max(cur_val + left, cur_val + right, cur_val) #either return left path, right path, or just the node val itself
        
        findMax(root)
        return result