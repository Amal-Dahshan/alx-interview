#!/usr/bin/python3
""" Prime game """


def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def remove_multiples(nums, prime):
    """Removes the prime and its multiples from the list."""
    new_nums = []
    for num in nums:
        if num % prime != 0:
            new_nums.append(num)
    return new_nums


def isWinner(x, nums):
    """Determines the winner of a game."""
    maria_wins = 0
    ben_wins = 0
    for _ in range(x):
        player = "Maria"
        while nums:
            if player == "Maria":
                # Find first prime in the list
                for num in nums:
                    if is_prime(num):
                        nums = remove_multiples(nums, num)
                        player = "Ben"
                        break
            else:
                # Ben has no choice but to pick the first number
                nums = remove_multiples(nums, nums[0])
                player = "Maria"
        if nums:
            ben_wins += 1
        else:
            maria_wins += 1
        nums = list(range(1, max(nums) + 1))  # Reset for next round
    return "Maria" if maria_wins > ben_wins else ("Ben" if ben_wins > maria_wins else None)
