class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        // The center node must be one of the nodes in the first edge
        int candidate1 = edges[0][0];
        int candidate2 = edges[0][1];

        // Check which candidate appears in the second edge
        if (edges[1][0] == candidate1 || edges[1][1] == candidate1) {
            return candidate1;
        }
        return candidate2;
    }
        
};