class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        
        # Calculate the initial satisfaction without using the technique
        initial_satisfaction = 0
        for i in range(n):
            if grumpy[i] == 0:
                initial_satisfaction += customers[i]
        
        # Calculate the initial potential gain with the first window
        max_gain = 0
        current_gain = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                current_gain += customers[i]
        
        max_gain = current_gain
        
        # Slide the window across the array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                current_gain += customers[i]
            if grumpy[i - minutes] == 1:
                current_gain -= customers[i - minutes]
            max_gain = max(max_gain, current_gain)
        
        # The total satisfied customers is the initial satisfaction plus the max_gain
        return initial_satisfaction + max_gain


        