class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1  # Sequence length
        res = [0] * size  # Result array initialized with 0
        used = set()  # Track used numbers

        def backtrack(index: int) -> bool:
            """Try to construct the sequence starting from index."""
            if index == size:  # If all positions are filled
                return True
            
            if res[index] != 0:  # Skip already filled positions
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):  # Try placing largest first
                if num in used:  # Already used
                    continue
                
                if num == 1:  # Place '1' in the first available spot
                    res[index] = 1
                    used.add(1)
                    if backtrack(index + 1): 
                        return True
                    res[index] = 0
                    used.remove(1)
                
                else:
                    second_index = index + num  # Calculate second occurrence index
                    if second_index < size and res[second_index] == 0:
                        # Place 'num' at both positions
                        res[index] = res[second_index] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        # Undo placement (Backtrack)
                        res[index] = res[second_index] = 0
                        used.remove(num)

            return False  # No valid placement found
        
        backtrack(0)
        return res