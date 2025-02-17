class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)  # Count frequency of each character

        def backtrack():
            count = 0
            for ch in freq:
                if freq[ch] > 0:
                    freq[ch] -= 1  # Choose letter
                    count += 1 + backtrack()  # Add valid sequence and recurse
                    freq[ch] += 1  # Backtrack (restore count)
            return count

        return backtrack()
        