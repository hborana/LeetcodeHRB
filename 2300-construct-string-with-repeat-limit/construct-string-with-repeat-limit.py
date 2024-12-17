import heapq
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Frequency count and initialize max heap
        freq = Counter(s)
        max_heap = [(-ord(char), count) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            # Get the largest character
            char_neg, count = heapq.heappop(max_heap)
            char = chr(-char_neg)
            
            # Determine how many times we can use it
            use_count = min(repeatLimit, count)
            result.extend([char] * use_count)
            count -= use_count
            
            if count > 0:
                # If we have more of the current character, we need to "break" the sequence
                if not max_heap:
                    break  # No other characters available, we stop here
                
                # Take the next largest character
                next_char_neg, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char_neg)
                
                # Use the next character once to break the limit
                result.append(next_char)
                next_count -= 1
                
                # Push back both characters into the heap with updated counts
                heapq.heappush(max_heap, (-ord(char), count))
                if next_count > 0:
                    heapq.heappush(max_heap, (-ord(next_char), next_count))
            # If no more of the current character, just continue
            
        return ''.join(result)