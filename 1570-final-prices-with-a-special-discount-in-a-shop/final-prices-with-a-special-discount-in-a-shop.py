class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = prices[:]  # Create a copy of the prices array for the answer

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break  # Discount found, move to the next item

        return answer