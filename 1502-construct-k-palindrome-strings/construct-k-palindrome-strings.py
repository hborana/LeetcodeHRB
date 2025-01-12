class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
         # Step 1: Count character frequencies
        char_count = Counter(s)
        
        # Step 2: Count characters with odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # Step 3: Check conditions
        # - If odd_count > k, it's impossible to form k palindromes
        # - If len(s) < k, it's impossible to form k palindromes
        if odd_count > k or len(s) < k:
            return False
        
        return True

        