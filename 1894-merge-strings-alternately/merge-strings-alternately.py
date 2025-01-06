class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i, j = 0, 0
        n, m = len(word1), len(word2)

        # Alternate between characters of word1 and word2
        while i < n and j < m:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters from the longer string
        if i < n:
            merged.append(word1[i:])
        if j < m:
            merged.append(word2[j:])

        return ''.join(merged)
            