class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
    
        # Step 1: Reverse the graph
        reverse_graph = defaultdict(list)
        indegree = [0] * n
        
        for src in range(n):
            for dest in graph[src]:
                reverse_graph[dest].append(src)
                indegree[src] += 1
        
        # Step 2: Topological sort using a queue
        queue = deque([i for i in range(n) if indegree[i] == 0])
        safe_nodes = []
        
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Return sorted list of safe nodes
        return sorted(safe_nodes)