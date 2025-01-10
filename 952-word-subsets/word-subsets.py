class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # Find the maximum frequency of each character required in words2
        max_freq = Counter()
        for word in words2:
            freq = Counter(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])
        
        # Check if a word from words1 is universal
        def isUniversal(word):
            freq = Counter(word)
            for char, count in max_freq.items():
                if freq[char] < count:
                    return False
            return True
        
        # Return all universal words in words1
        return [word for word in words1 if isUniversal(word)]