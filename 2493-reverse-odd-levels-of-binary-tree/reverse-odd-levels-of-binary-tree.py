# Definition for a binary tree node.
from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # BFS to traverse the tree and collect nodes level by level
        queue = deque([root])
        level = 0
        levels = []  # Store values at each level

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level)
            level += 1

        # Reverse values at odd levels
        for i in range(1, len(levels), 2):  # Odd levels
            values = [node.val for node in levels[i]]
            values.reverse()
            for j, node in enumerate(levels[i]):
                node.val = values[j]

        return root
            