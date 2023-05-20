# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def compute(root, leftmax, rightmax):
            if(root== None): return True
            
            if(leftmax<root.val<rightmax): return compute(root.left,leftmax,root.val) and compute(root.right,root.val,rightmax)
            
            return False
        
        return compute(root, float('-inf'),float('inf'))
        