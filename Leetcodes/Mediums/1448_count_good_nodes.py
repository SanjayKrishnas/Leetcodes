# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #in order traversal
        result = 0

        def countGoodNodes(root, rel_max):
            nonlocal result
            if root == None: return

            #process cur node
            if root.val >= rel_max:
                result += 1
            
            #recurse
            countGoodNodes(root.left, max(rel_max, root.val))
            countGoodNodes(root.right, max(rel_max, root.val))

        countGoodNodes(root, -float('inf'))
        return result