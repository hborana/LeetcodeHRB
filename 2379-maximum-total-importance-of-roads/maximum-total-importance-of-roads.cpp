class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<int> degree(n, 0);
        
        // Count the degree of each city
        for (const auto& road : roads) {
            degree[road[0]]++;
            degree[road[1]]++;
        }
        
        // Pair each city with its degree
        vector<pair<int, int>> cityDegree;
        for (int i = 0; i < n; ++i) {
            cityDegree.push_back({degree[i], i});
        }
        
        // Sort cities based on their degree in descending order
        sort(cityDegree.begin(), cityDegree.end(), greater<pair<int, int>>());
        
        // Assign values to cities
        vector<int> values(n, 0);
        int currentValue = n;
        for (const auto& [deg, city] : cityDegree) {
            values[city] = currentValue--;
        }
        
        // Calculate the total importance of all roads
        long long totalImportance = 0;
        for (const auto& road : roads) {
            totalImportance += values[road[0]] + values[road[1]];
        }
        
        return totalImportance;
    }
};
