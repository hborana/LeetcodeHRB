#include <vector>
using namespace std;

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int consecutiveOddCount = 0;

        for (int num : arr) {
            if (num % 2 != 0) {
                // Current number is odd
                consecutiveOddCount++;
                if (consecutiveOddCount == 3) {
                    return true;
                }
            } else {
                // Current number is even
                consecutiveOddCount = 0;
            }
        }

        return false;
    }
};

