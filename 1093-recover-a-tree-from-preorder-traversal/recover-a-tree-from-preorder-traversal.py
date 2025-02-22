# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        
        while i < len(traversal):
            depth = 0
            # Count the number of dashes to determine depth
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Extract the number
            num_start = i
            while i < len(traversal) and traversal[i].isdigit():
                i += 1
            num = int(traversal[num_start:i])
            
            # Create the new node
            node = TreeNode(num)
            
            # If the stack is larger than depth, pop to find the correct parent
            while len(stack) > depth:
                stack.pop()
            
            # Attach node as a child
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Push this node onto the stack
            stack.append(node)
        
        # The root is the first element in the stack
        return stack[0]

    # Example Usage:
    def preorder_traversal(root):
        return [root.val] + preorder_traversal(root.left) if root.left else [] + preorder_traversal(root.right) if root.right else []

            