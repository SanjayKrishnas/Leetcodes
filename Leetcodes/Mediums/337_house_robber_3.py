class Solution:
    def __init__(self):  # Fixed: added self parameter
        self.cache = {}
        
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:  # Fixed: use 'is None' instead of '== None'
            return 0

        if root in self.cache: 
            return self.cache[root]

        # Option 1: Rob this house
        rob_current = root.val
        if root.left is not None:
            rob_current += self.rob(root.left.left)  # Fixed: added self.
            rob_current += self.rob(root.left.right)  # Fixed: need both grandchildren
        if root.right is not None:
            rob_current += self.rob(root.right.left)   # Fixed: need both grandchildren
            rob_current += self.rob(root.right.right)  # Fixed: added self.

        # Option 2: Don't rob this house
        dont_rob_current = self.rob(root.left) + self.rob(root.right)  # Fixed: added left child

        self.cache[root] = max(rob_current, dont_rob_current)
        return self.cache[root]
    