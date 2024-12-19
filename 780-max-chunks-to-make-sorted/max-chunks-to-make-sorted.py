class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen = 0
        chunks = 0
        
        for i, value in enumerate(arr):
            max_seen = max(max_seen, value)
            # If the max value seen so far equals the index, we can make a chunk
            if max_seen == i:
                chunks += 1
        
        return chunks