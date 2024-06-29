class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        // Initialize the adjacency list
        vector<vector<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[1]].push_back(edge[0]);
        }
        
        // Initialize a list of sets to store ancestors for each node
        vector<unordered_set<int>> ancestors(n);
        
        // Function to perform DFS and find ancestors
        function<void(int)> dfs = [&](int node) {
            for (int neighbor : graph[node]) {
                if (ancestors[node].count(neighbor) == 0) {
                    ancestors[node].insert(neighbor);
                    dfs(neighbor);
                    ancestors[node].insert(ancestors[neighbor].begin(), ancestors[neighbor].end());
                }
            }
        };
        
        // Perform DFS from each node
        for (int i = 0; i < n; ++i) {
            dfs(i);
        }
        
        // Convert sets to sorted lists
        vector<vector<int>> result(n);
        for (int i = 0; i < n; ++i) {
            result[i] = vector<int>(ancestors[i].begin(), ancestors[i].end());
            sort(result[i].begin(), result[i].end());
        }
        
        return result;
    }
};