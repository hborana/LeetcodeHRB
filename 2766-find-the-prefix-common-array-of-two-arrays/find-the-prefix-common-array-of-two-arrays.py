class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Sets to track seen elements in A and B
        seen_A = set()
        seen_B = set()
        # Resultant prefix common array
        C = []
        
        for i in range(len(A)):
            # Update the sets with current elements from A and B
            seen_A.add(A[i])
            seen_B.add(B[i])
            # Find the intersection and calculate its size
            common_count = len(seen_A.intersection(seen_B))
            # Append the count to C
            C.append(common_count)
        
        return C
