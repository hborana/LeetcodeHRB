class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr):
            if len(curr) == n:
                happy_strings.append(curr)
                return
            
            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch: 
                    backtrack(curr + ch)

        happy_strings = []
        backtrack("")
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""

            