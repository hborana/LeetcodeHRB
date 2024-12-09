import java.util.ArrayList;
import java.util.List;

public class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;
        List<Integer> store = new ArrayList<>();
        List<Boolean> ans = new ArrayList<>();

        // Step 1: Store indices where adjacent elements have the same parity
        for (int i = 1; i < n; i++) {
            if ((nums[i] % 2) == (nums[i - 1] % 2)) {
                store.add(i - 1); // Store the starting index of the mismatch pair
            }
        }

        // Step 2: Process each query
        for (int[] query : queries) {
            int left = query[0];
            int right = query[1];

            // Binary search for the first index in `store` >= `left`
            int idx = binarySearch(store, left - 1);

            // Check if a parity mismatch exists in the range [left, right]
            if (idx < store.size() && store.get(idx) < right) {
                ans.add(false); // Mismatch exists in the range
            } else {
                ans.add(true);
            }
        }

        // Convert List<Boolean> to boolean[] before returning
        boolean[] result = new boolean[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            result[i] = ans.get(i);
        }

        return result;
    }

    // Binary search to find the first element >= target
    private int binarySearch(List<Integer> store, int target) {
        int low = 0, high = store.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (store.get(mid) <= target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
}
