class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        
        # Count the elements in nums1 and nums2
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Result list to store the intersection
        result = []
        
        # Iterate through the counts in count1
        for num in count1:
            if num in count2:
                # Add the minimum count of the element to the result
                result.extend([num] * min(count1[num], count2[num]))
        
        return result

