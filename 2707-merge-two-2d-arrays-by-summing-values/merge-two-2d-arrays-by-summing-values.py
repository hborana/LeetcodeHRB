class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged_dict = {}
    
        # Process nums1
        for idi, vali in nums1:
            merged_dict[idi] = merged_dict.get(idi, 0) + vali
        
        # Process nums2
        for idi, vali in nums2:
            merged_dict[idi] = merged_dict.get(idi, 0) + vali
        
        # Convert dictionary to sorted list
        result = sorted(merged_dict.items())
        
        return result