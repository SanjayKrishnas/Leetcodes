# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #Use recursion

        if root == None: return None

        if root.val == key:
            if root.right == None:
                return root.left
            elif root.left == None:
                return root.right
            
            #ELSE WE CHOOSE TO REPLACE WITH MIN VALUE ON RIGHT SIDE

            cur = root.right
            while cur.left:
                cur = cur.left
            self.deleteNode(root, cur.val)
            root.val = cur.val

        elif root.val > key: #go left
            root.left = self.deleteNode(root.left, key)
        else: #go right
            root.right = self.deleteNode(root.right, key)

        return root
        
        