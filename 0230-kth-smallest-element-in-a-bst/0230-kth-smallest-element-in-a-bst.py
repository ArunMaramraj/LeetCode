# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ele = 0
        def compute(root):
            if(root==None):
                return None

            result=compute(root.left)
            if result is not None:
                return result
            
            self.ele+=1
            
            if(self.ele==self.k):
                return root.val
            
            return compute(root.right)
        return compute(root)
        