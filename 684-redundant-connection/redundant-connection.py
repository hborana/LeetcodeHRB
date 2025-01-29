class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n + 1))  # Parent array
        self.rank = [1] * (n + 1)  # Rank array for union by rank

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False  # Cycle detected
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        uf = UnionFind(n)
        
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge  # The redundant edge

    # def findRedundantConnection(self, edges):
       
        