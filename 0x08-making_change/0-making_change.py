#!/usr/bin/python3
""" making change """


def makeChange(coins, total):
  """
  This function determines the fewest number of coins needed to meet a given amount.

  Args:
      coins: A list of integer coin values.
      total: The target amount to reach using coins.

  Returns:
      The fewest number of coins needed to reach the target amount, or -1 if not possible.
  """

  # Base cases
  if total == 0:
    return 0
  if total < 0:
    return -1

  # Dynamic programming approach: dp[i] represents the minimum coins needed for amount i
  dp = [float('inf')] * (total + 1)
  dp[0] = 0  # 0 amount requires 0 coins

  # Iterate through each coin value
  for coin in coins:
    # Iterate through all amounts up to the total
    for amount in range(coin, total + 1):
      # Update dp[amount] if using the current coin results in a smaller number of coins
      dp[amount] = min(dp[amount], dp[amount - coin] + 1)

  # Check if the target amount can be reached
  return dp[total] if dp[total] != float('inf') else -1

# Example usage (uncomment for testing)
# coins = [1, 5, 10, 25]
# total = 38
# result = makeChange(coins, total)
# print(f"Minimum coins needed for {total}: {result}")
