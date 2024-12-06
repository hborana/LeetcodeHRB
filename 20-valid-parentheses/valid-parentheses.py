class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')':'(','}':'{',']':'['}
        stack = []

        for char in s:
            if char in brackets:
                top_ele = stack.pop() if stack else '#'
                if brackets[char] != top_ele:
                    return False
            else:
                stack.append(char)

        return not stack