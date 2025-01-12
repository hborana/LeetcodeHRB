class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        # Left-to-right pass
        open_count = 0
        flexible_count = 0
        for i in range(len(s)):
            if locked[i] == '0':
                flexible_count += 1
            elif s[i] == '(':
                open_count += 1
            else:  # s[i] == ')'
                if open_count > 0:
                    open_count -= 1
                elif flexible_count > 0:
                    flexible_count -= 1
                else:
                    return False  # Too many `)` without matching `(`
        
        # Right-to-left pass
        close_count = 0
        flexible_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                flexible_count += 1
            elif s[i] == ')':
                close_count += 1
            else:  # s[i] == '('
                if close_count > 0:
                    close_count -= 1
                elif flexible_count > 0:
                    flexible_count -= 1
                else:
                    return False  # Too many `(` without matching `)`
        
        return True

        