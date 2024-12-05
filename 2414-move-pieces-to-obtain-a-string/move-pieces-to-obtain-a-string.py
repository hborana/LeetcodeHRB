class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        # Remove blanks and compare the sequence of 'L' and 'R'
        start_pieces = ''.join(c for c in start if c != '_')
        target_pieces = ''.join(c for c in target if c != '_')
        if start_pieces != target_pieces:
            return False

        # Check positions of 'L' and 'R'
        start_pos = [(c, i) for i, c in enumerate(start) if c != '_']
        target_pos = [(c, i) for i, c in enumerate(target) if c != '_']
        
        for (start_char, start_idx), (target_char, target_idx) in zip(start_pos, target_pos):
            if start_char == 'L' and start_idx < target_idx:
                return False  # 'L' can only move left
            if start_char == 'R' and start_idx > target_idx:
                return False  # 'R' can only move right
        
        return True
            