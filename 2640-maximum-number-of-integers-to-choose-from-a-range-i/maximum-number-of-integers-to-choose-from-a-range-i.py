class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)
        total_sum = 0
        count = 0
        
        # Step 2: Iterate over numbers from 1 to n
        for num in range(1, n + 1):
            if num not in banned_set:  # Check if the number is not banned
                if total_sum + num > maxSum:  # Stop if adding the number exceeds maxSum
                    break
                total_sum += num  # Add the number to the sum
                count += 1  # Increment the count
        
        # Step 3: Return the count of selected numbers
        return count
        