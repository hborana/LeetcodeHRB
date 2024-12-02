class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()

        for index, word in enumerate(words):
            if word.startswith(searchWord):
                return index + 1

        return -1
        