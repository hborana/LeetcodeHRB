class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['']
        
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                top = stack.pop()
                stack[-1] += top[::-1]
            else:
                stack[-1] += char
        
        return stack[0]
        