class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        # Initialize indegree array
        indegree = [0] * n
        
        # Calculate indegree for each node
        for u, v in edges:
            indegree[v] += 1
        
        # Find nodes with indegree 0
        champions = [i for i in range(n) if indegree[i] == 0]
        
        # If there is exactly one champion, return it
        if len(champions) == 1:
            return champions[0]
        
        # Otherwise, return -1
        return -1