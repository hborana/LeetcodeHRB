class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Base case :
        if not str:
            return ""

        
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix
