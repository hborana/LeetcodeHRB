"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def _dfs(node):
            if node is None:
                return 

            for child in node.children:
                _dfs(child)
            
            result.append(node.val)

        _dfs(root)

        return result 
