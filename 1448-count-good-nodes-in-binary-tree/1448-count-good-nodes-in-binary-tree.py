# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self,count=0):
        self.count = count
        
    def goodNodes(self, root: TreeNode) -> int:
                
        def compute(root,maxVal):
            
            if (root==None):
                return    
            
            if(root.val >= maxVal):
                self.count+=1
                
            compute(root.left,max(root.val,maxVal))
            compute(root.right,max(root.val,maxVal))
            
            
        compute(root, float(-inf))
        
        return self.count

            
           