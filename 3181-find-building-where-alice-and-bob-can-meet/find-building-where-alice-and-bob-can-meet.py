from heapq import heappush, heappop
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(heights)
        q = len(queries)
        result = [-1] * q
        deferred = [[] for _ in range(n)]
        pq = []  # Min-heap

        for i in range(q):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                result[i] = b
            else:
                deferred[b].append((heights[a], i))

        for i in range(n):
            for query in deferred[i]:
                heappush(pq, query)
            while pq and pq[0][0] < heights[i]:
                _, idx = heappop(pq)
                result[idx] = i

        return result