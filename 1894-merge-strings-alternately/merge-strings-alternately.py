class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0
        len1 = len(word1)
        len2 = len(word2)

        while i < len1 or j < len2:
            if i < len1:
                merged.append(word1[i])
                i += 1
            if j < len2:
                merged.append(word2[j])
                j += 1 

        return ''.join(merged)
        