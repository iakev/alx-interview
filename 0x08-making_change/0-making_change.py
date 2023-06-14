#!/usr/bin/python3
"""
Containing the classic fewest number of coins needed o meet a specified
"""


def makeChange(coins, total):
    """
    coins: list of values of coins currently in possesion
    total: Amount to be given as change
    Returns: fewest number of coins needed to meet total
             if total is <= 0 return 0
             if total can't be met by coins return -1
    Assumption: Infinite number of each coin denomination in list
                Value of coin will always be greater than zero
    """
    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)
    no_of_coins = recursive_make_change(sorted_coins, total, 0)
    return no_of_coins


def recursive_make_change(coins, total, no_of_coins):
    """
    Recursive helper function to implement makeChange function
    coins: list of values of coins currently in possesion successively
           decreasing it's lenght on each recursive call
    total: Amount to be given as change, succesively decreasing to zero
           with each succesive call
    Returns: no_of_coins
    """
    if total == 0:
        return no_of_coins
    if total != 0 and len(coins) == 0:
        no_of_coins = -1
        return no_of_coins
    if total >= coins[0]:
        new_total = total % coins[0]
        if new_total == 0:
            no_of_coins += total // coins[0]
            no_of_coins = recursive_make_change(coins[1:],
                                                new_total, no_of_coins)
        else:
            no_of_coins += 1
            no_of_coins = recursive_make_change(coins[1:],
                                                new_total, no_of_coins)
    else:
        no_of_coins = recursive_make_change(coins[1:],
                                            total, no_of_coins)
    return no_of_coins
