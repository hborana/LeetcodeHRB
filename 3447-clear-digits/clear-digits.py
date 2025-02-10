class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()  # Remove closest non-digit
            else:
                stack.append(char)  # Store non-digit characters
        
        return "".join(stack)
