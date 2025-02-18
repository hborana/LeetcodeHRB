class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        num = 1  # Start from smallest available digit

        for i, ch in enumerate(pattern + 'I'):  # Append 'I' to flush out remaining stack
            stack.append(str(num))  # Push the current number
            num += 1

            if ch == 'I':  # When encountering 'I' or end, pop stack to result
                while stack:
                    result.append(stack.pop())

        return "".join(result)

        