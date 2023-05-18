# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.booli = False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if (p and not q) or (not p and q):
                return False
            if not p and not q:
                return True
            if p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            return False
    
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        
        if self.booli:
            return True
        
        if isSameTree(root, subRoot):
            self.booli = True
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        