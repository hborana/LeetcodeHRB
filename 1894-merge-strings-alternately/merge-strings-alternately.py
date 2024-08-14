class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        min_Len = min(len(word1),len(word2))

        for i in range(min_Len):
            merged += word1[i] + word2[i]

        merged += word1[min_Len:] + word2[min_Len:]

        return merged 

        