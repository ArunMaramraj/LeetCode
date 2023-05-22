# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        
        def compute(root):
            if root==None: return 0
            
            leftsum = max(0,compute(root.left))
            rightsum = max(0,compute(root.right))
            
            self.maxi = max(self.maxi, root.val + leftsum + rightsum)
            
            return root.val + max(leftsum , rightsum)
        
        compute(root)
        return self.maxi