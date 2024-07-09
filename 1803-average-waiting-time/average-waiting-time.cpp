#include <vector>
using namespace std;

class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long long current_time = 0;
        long long total_waiting_time = 0;

        for (const auto& customer : customers) {
            int arrival = customer[0];
            int time_needed = customer[1];

            if (current_time < arrival) {
                current_time = arrival;
            }
            current_time += time_needed;
            total_waiting_time += (current_time - arrival);
        }

        return static_cast<double>(total_waiting_time) / customers.size();
    }
};