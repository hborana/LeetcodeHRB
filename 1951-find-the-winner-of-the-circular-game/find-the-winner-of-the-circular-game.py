class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = list(range(1, n + 1))
        current_index = 0
        
        while len(friends) > 1:
            current_index = (current_index + k - 1) % len(friends)
            friends.pop(current_index)
        
        return friends[0]
        