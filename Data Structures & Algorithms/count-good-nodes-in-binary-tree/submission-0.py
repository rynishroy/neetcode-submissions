# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
         
        #run dfs and pass maxValue for every node , check if node value is greater than maxValue
      #add it to res
        def dfs(node, maxValue):
            if not node:
                return 0

            maxValue = max(maxValue, node.val)
            res = 1 if node.val >= maxValue else 0
            res += dfs(node.left, maxValue)
            res +=dfs(node.right, maxValue)
            return res
        
        return dfs(root, float("-inf"))
        