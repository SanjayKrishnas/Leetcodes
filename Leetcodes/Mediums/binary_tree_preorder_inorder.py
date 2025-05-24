# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #the first node in the preorder list will be the current node
        #then we divide the inorder list by that value and split it into a left and rigth subtree and recurse
        if not preorder or not inorder: return None

        curNode = TreeNode(preorder[0])

        #find where to split the inorder traversal
        index = 0
        while inorder[index] != preorder[0]:
            index += 1
        
        leftPre = preorder[1:index+1]
        rightPre = preorder[index+1:]
        leftIn = inorder[:index]
        rightIn = inorder[index+1:]

        curNode.left = self.buildTree(leftPre, leftIn)
        curNode.right = self.buildTree(rightPre, rightIn)

        return curNode