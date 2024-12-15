import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    # Function to calculate the gain of adding one student
        def gain(passi, totali):
            return (passi + 1) / (totali + 1) - passi / totali

        # Max heap (negative of gain for max-heap behavior in Python)
        heap = []
        for passi, totali in classes:
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
        
        # Assign extra students
        for _ in range(extraStudents):
            # Pop class with the highest gain
            max_gain, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            # Push updated class back into the heap
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
        
        # Calculate the average pass ratio
        total_ratio = 0
        for _, passi, totali in heap:
            total_ratio += passi / totali
        
        return total_ratio / len(classes)