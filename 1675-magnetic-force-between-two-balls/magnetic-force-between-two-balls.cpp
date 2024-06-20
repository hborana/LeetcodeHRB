#include <vector>
#include <algorithm>

class Solution {
public:
    int maxDistance(std::vector<int>& position, int m) {
        // Step 1: Sort the positions
        std::sort(position.begin(), position.end());

        // Step 2: Initialize binary search bounds
        int left = 1; // Minimum possible distance
        int right = position.back() - position.front(); // Maximum possible distance

        // Helper function to check feasibility
        auto canPlaceBalls = [&](int minDist) -> bool {
            int count = 1; // Place the first ball at the first basket
            int last_position = position[0];

            for (int i = 1; i < position.size(); ++i) {
                if (position[i] - last_position >= minDist) {
                    count++;
                    last_position = position[i];
                    if (count >= m) {
                        return true;
                    }
                }
            }
            return false;
        };

        // Step 3: Binary search to maximize the minimum distance
        while (left < right) {
            int mid = left + (right - left + 1) / 2; // Midpoint to avoid infinite loop
            if (canPlaceBalls(mid)) {
                left = mid; // Try for a larger distance
            } else {
                right = mid - 1; // Try for a smaller distance
            }
        }

        return left;
    }
};