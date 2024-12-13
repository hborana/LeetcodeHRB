import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = [False] * len(nums)
        pq = []
        
        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))
        
        while pq:
            num, i = heapq.heappop(pq)
            
            if not marked[i]:
                score += num
                marked[i] = True
                
                if i > 0 and not marked[i - 1]:
                    marked[i - 1] = True
                    heapq.heappush(pq, (nums[i - 1], i - 1))
                
                if i < len(nums) - 1 and not marked[i + 1]:
                    marked[i + 1] = True
                    heapq.heappush(pq, (nums[i + 1], i + 1))
        
        return score