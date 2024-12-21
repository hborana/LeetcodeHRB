from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
         # Step 1: Build adjacency list
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        # Step 2: Initialize variables
        visited = [False] * n
        valid_splits = 0

        # Step 3: DFS function
        def dfs(node):
            nonlocal valid_splits
            visited[node] = True
            subtree_sum = values[node]  # Start with the current node's value

            for neighbor in tree[node]:
                if not visited[neighbor]:
                    child_sum = dfs(neighbor)  # Compute subtree sum for the child
                    # Check if the child's subtree sum is divisible by k
                    if child_sum % k == 0:
                        valid_splits += 1  # Split at this edge
                    else:
                        subtree_sum += child_sum  # Accumulate to parent's sum
            
            return subtree_sum

        # Step 4: Run DFS starting from node 0
        dfs(0)

        # The number of components is the valid splits + 1 (root component)
        return valid_splits + 1