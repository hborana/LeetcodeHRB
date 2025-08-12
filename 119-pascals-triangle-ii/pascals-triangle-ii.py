class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for k in range(1, rowIndex + 1):
            # Use formula to compute next number from previous one
            next_val = row[-1] * (rowIndex - k + 1) // k
            row.append(next_val)
        return row
            