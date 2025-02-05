class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
         # Step 1: If strings are already equal, return True
        if s1 == s2:
            return True

        # Step 2: Find indices where s1 and s2 differ
        diff = [(s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]

        # Step 3: There must be exactly 2 differences, and they must be swappable
        return len(diff) == 2 and diff[0] == diff[1][::-1]
        