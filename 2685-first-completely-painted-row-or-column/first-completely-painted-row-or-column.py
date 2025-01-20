class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)

        rowPainted = [0] * m
        colPainted = [0] * n
        
        for idx, num in enumerate(arr):
            row, col = position[num]
            rowPainted[row] += 1
            colPainted[col] += 1
            
            if rowPainted[row] == n or colPainted[col] == m:
                return idx
        
        return -1  