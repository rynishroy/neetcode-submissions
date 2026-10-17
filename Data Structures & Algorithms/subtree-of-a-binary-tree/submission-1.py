# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if subroot is null ,then it is subtree
        if not subRoot:
            return True
        
        #if first main tree then its False
        if not root:
            return False
        
        #if both tree are same
        if self.isSameTree(root,subRoot):
            return True
    
        #check for root left and right
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self,s, t):
        if not s and not t:
            return True
            
        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right))
        return False

        