class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Step 1: Build the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Find Bob's path to root
        def find_bob_path(node, parent, path):
            if node == 0:
                path.append(node)
                return True
            for neighbor in tree[node]:
                if neighbor != parent and find_bob_path(neighbor, node, path):
                    path.append(node)
                    return True
            return False
        
        bob_path = []
        find_bob_path(bob, -1, bob_path)
        bob_path.reverse()
        
        # Map node to time Bob reaches it
        bob_time = {node: t for t, node in enumerate(bob_path)}
        
        # Step 3: DFS to find max profit for Alice
        def dfs(node, parent, time, current_income):
            if node in bob_time:
                if bob_time[node] < time:
                    contribution = 0  # Bob already passed
                elif bob_time[node] == time:
                    contribution = amount[node] // 2  # Split reward/cost
                else:
                    contribution = amount[node]  # Alice alone
            else:
                contribution = amount[node]
            
            current_income += contribution
            
            # Check if leaf node
            children = [child for child in tree[node] if child != parent]
            if not children:
                return current_income
            
            # Recur for child nodes and get max
            return max(dfs(child, node, time + 1, current_income) for child in children)
        
        return dfs(0, -1, 0, 0)
