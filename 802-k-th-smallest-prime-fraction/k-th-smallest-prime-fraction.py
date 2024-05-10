from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Initialize the min-heap
        heap = [(arr[i] / arr[j], i, j) for i in range(len(arr) - 1) for j in  range(i + 1, len(arr))]
        heapq.heapify(heap)
        
        # Pop from the heap k-1 times to reach the k-th smallest fraction
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
        
        # The k-th smallest element is now the root of the min-heap
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]

        