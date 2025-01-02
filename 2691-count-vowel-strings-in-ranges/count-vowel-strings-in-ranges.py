class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Helper function to check if a string starts and ends with a vowel
        def is_vowel_string(s):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return s[0] in vowels and s[-1] in vowels

        # Create the prefix sum array
        n = len(words)
        prefix = [0] * n
        prefix[0] = 1 if is_vowel_string(words[0]) else 0
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + (1 if is_vowel_string(words[i]) else 0)
        
        # Process each query
        result = []
        for li, ri in queries:
            if li == 0:
                result.append(prefix[ri])
            else:
                result.append(prefix[ri] - prefix[li - 1])
        
        return result
