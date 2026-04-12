class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_target = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                new_target = prices[j] - prices[i]
                if new_target > max_target:
                    max_target = new_target
        return max_target
        