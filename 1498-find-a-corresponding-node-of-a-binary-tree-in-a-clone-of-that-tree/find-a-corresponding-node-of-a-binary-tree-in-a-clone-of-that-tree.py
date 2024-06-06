# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Base Case : If there is no Original node 
        if not original:
            return None
        
        if original == target:
            return cloned

        result = self.getTargetCopy(original.left, cloned.left, target)
        if result:
            return result

        return self.getTargetCopy(original.right, cloned.right, target)   
