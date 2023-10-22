class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 

        count_S = {}
        count_T = {}

        for i in range(len(s)):
            count_S[s[i]] = 1 + count_S.get(s[i],0)
            count_T[t[i]] = 1 + count_T.get(t[i],0)

        for c in count_S:
            if count_S[c] != count_T.get(c,0):
                return False

        return True

        