class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        answer = [0] * n

        # Forward pass
        left_operations = 0
        left_balls = 0
        for i in range(n):
            answer[i] += left_operations
            left_balls += int(boxes[i])  # Add current box's balls
            left_operations += left_balls  # Increment operations for the next step

        # Backward pass
        right_operations = 0
        right_balls = 0
        for i in range(n - 1, -1, -1):
            answer[i] += right_operations
            right_balls += int(boxes[i])  # Add current box's balls
            right_operations += right_balls  # Increment operations for the next step

        return answer
            