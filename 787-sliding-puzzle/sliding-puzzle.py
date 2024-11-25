from collections import deque
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        target = "123450"
    
        # Convert the board into a single string representation
        start = "".join(str(num) for row in board for num in row)
        
        # Possible moves based on 2x3 grid
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS setup
        queue = deque([(start, 0)])  # (current state, number of moves)
        visited = set()  # To keep track of visited states
        visited.add(start)
        
        while queue:
            state, steps = queue.popleft()
            
            # Check if the target state is reached
            if state == target:
                return steps
            
            # Find the position of '0' (empty tile)
            zero_pos = state.index("0")
            
            # Try all possible swaps
            for swap_pos in moves[zero_pos]:
                # Create the new state by swapping
                new_state = list(state)
                new_state[zero_pos], new_state[swap_pos] = new_state[swap_pos], new_state[zero_pos]
                
                new_state = "".join(new_state)
                
                # If the new state is not visited, add it to the queue
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
        
        # If no solution is found
        return -1
