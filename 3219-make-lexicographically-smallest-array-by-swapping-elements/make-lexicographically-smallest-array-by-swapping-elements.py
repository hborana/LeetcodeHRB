class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Step 1: Sort the input array
        sorted_nums = sorted(nums)

        # Initialize variables for grouping
        current_group = 0
        value_to_group = {sorted_nums[0]: current_group}
        group_to_elements = {current_group: deque([sorted_nums[0]])}

        # Step 2: Group elements based on the limit condition
        for i in range(1, len(sorted_nums)):
            # If the difference between consecutive elements exceeds the limit, start a new group
            if abs(sorted_nums[i] - sorted_nums[i - 1]) > limit:
                current_group += 1

            # Assign the current element to its group
            value_to_group[sorted_nums[i]] = current_group

            # Add the element to the appropriate group's deque
            if current_group not in group_to_elements:
                group_to_elements[current_group] = deque()
            group_to_elements[current_group].append(sorted_nums[i])

        # Step 3: Reconstruct the original array using the sorted groups
        for i in range(len(nums)):
            num = nums[i]
            group = value_to_group[num]  # Find the group of the current number
            nums[i] = group_to_elements[group].popleft()  # Replace with the smallest unused element in the group

        return nums
