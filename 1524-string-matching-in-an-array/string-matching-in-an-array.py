class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        # Iterate over each pair of words
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and word1 in word2:  # Check if word1 is a substring of word2
                    result.append(word1)
                    break  # No need to check further if we already found a match

        return result