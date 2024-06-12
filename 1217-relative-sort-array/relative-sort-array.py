class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to store the order of elements in arr2
        order_dict = {num: index for index, num in enumerate(arr2)}
        
        # Define the custom sort key
        def custom_sort_key(num):
            if num in order_dict:
                return (order_dict[num], num)
            else:
                return (len(arr2), num)
        
        # Sort arr1 using the custom sort key
        arr1.sort(key=custom_sort_key)
        
        return arr1
        