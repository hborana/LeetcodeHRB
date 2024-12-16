
# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        # result = []

        # def traverse(node):
        #     if node:
        #         traverse(node.left)
        #         result.append(node.val)
        #         traverse(node.right)
            
        # traverse(root)
        # return result 