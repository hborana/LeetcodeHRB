#include <vector>
#include <iostream>
using namespace std;

class UnionFind {
public:
    UnionFind(int size) {
        parent.resize(size);
        rank.resize(size, 1);
        for (int i = 0; i < size; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX] += 1;
            }
            return true;
        }
        return false;
    }

private:
    vector<int> parent;
    vector<int> rank;
};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        UnionFind ufAlice(n + 1);
        UnionFind ufBob(n + 1);
        int removableEdges = 0;

        // Process type 3 edges first
        for (const auto& edge : edges) {
            if (edge[0] == 3) {
                bool usedAlice = ufAlice.unionSets(edge[1], edge[2]);
                bool usedBob = ufBob.unionSets(edge[1], edge[2]);
                if (!usedAlice && !usedBob) {
                    ++removableEdges;
                }
            }
        }

        // Process type 1 edges (Alice only)
        for (const auto& edge : edges) {
            if (edge[0] == 1) {
                if (!ufAlice.unionSets(edge[1], edge[2])) {
                    ++removableEdges;
                }
            }
        }

        // Process type 2 edges (Bob only)
        for (const auto& edge : edges) {
            if (edge[0] == 2) {
                if (!ufBob.unionSets(edge[1], edge[2])) {
                    ++removableEdges;
                }
            }
        }

        // Check if both Alice and Bob can fully traverse the graph
        if (isFullyTraversable(ufAlice, n) && isFullyTraversable(ufBob, n)) {
            return removableEdges;
        } else {
            return -1;
        }
    }

private:
    bool isFullyTraversable(UnionFind& uf, int n) {
        int root = uf.find(1);
        for (int i = 2; i <= n; ++i) {
            if (uf.find(i) != root) {
                return false;
            }
        }
        return true;
    }
};

// // Example usage
// int main() {
//     Solution solution;

//     int n1 = 4;
//     vector<vector<int>> edges1 = {{3, 1, 2}, {3, 2, 3}, {1, 1, 3}, {2, 2, 4}, {1, 3, 4}};
//     int result1 = solution.maxNumEdgesToRemove(n1, edges1);
//     // Expected output: 2
//     cout << "Maximum number of edges to remove: " << result1 << endl;

//     return 0;
// }
