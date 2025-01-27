class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
         # Step 1: Initialize the reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Step 2: Populate the reachability matrix with direct prerequisites
        for prereq in prerequisites:
            a, b = prereq
            reachable[a][b] = True
        
        # Step 3: Use Floyd-Warshall algorithm to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        # Step 4: Answer each query based on the reachability matrix
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        
        return result

            