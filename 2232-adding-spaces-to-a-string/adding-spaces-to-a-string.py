class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []
        space_index = 0  # Pointer for the spaces array

        for i in range(len(s)):
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(s[i])

        return ''.join(result)

        