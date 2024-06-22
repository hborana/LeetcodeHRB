#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        vector<int> odd_indices; // To store indices of odd numbers
        int n = nums.size();
        
        // Collect all odd number indices
        for (int i = 0; i < n; ++i) {
            if (nums[i] % 2 != 0) {
                odd_indices.push_back(i);
            }
        }
        
        int count = 0;
        
        // If there are less than k odd numbers, return 0
        if (odd_indices.size() < k) {
            return 0;
        }
        
        // Calculate the number of nice subarrays
        for (int i = 0; i <= odd_indices.size() - k; ++i) {
            int start = (i == 0) ? odd_indices[i] + 1 : odd_indices[i] - odd_indices[i-1];
            int end = (i + k == odd_indices.size()) ? n - odd_indices[i+k-1] : odd_indices[i+k] - odd_indices[i+k-1];
            count += start * end;
        }
        
        return count;
    }
};