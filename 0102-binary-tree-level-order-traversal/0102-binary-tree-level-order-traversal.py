# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if root is None : return []     
        queue = [root]
       
        output=[]       
        while queue:
            temp = []
            for i in queue : 
                temp.append(i.val)
            output.append(temp)
            templength = len(queue)
            while templength!=0:
                    temproot = queue.pop(0)
                    if(temproot.left is not None): queue.append(temproot.left)
                    if(temproot.right is not None): queue.append(temproot.right)
                    templength-=1
                   
        return output    