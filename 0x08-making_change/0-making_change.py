#!/usr/bin/python3
"""Determine the fewest number of coins
needed to meet a given amount
"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    # validity check
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    available_coins = sorted(coins, reverse=True)
    change_left = total

    for coin in available_coins:
        while (change_left % coin >= 0 and change_left >= coin):
            change += int(change_left / coin)
            change_left = change_left % coin

    change = change if change_left == 0 else -1

    return change
