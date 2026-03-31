# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def isBalancedRec(node: Optional[TreeNode]):

                if(node is None):
                        return 0
                if(node.left is None and node.right is None):
                        return 1

                right = isBalancedRec(node.right)
                left = isBalancedRec(node.left)
                if(abs(right - left) > 1 or right == -1 or left == -1):
                        return -1

                return 1 + max(right, left)  



        root_val = isBalancedRec(root)
        return root_val != -1
        