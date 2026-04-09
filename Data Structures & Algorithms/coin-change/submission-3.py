class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])

        return min_coins[amount] if min_coins[amount] != float('inf') else -1