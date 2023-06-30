#!/usr/bin/python3
"""
Module that contains various functions that
allow to play the Prime Game
"""


def bsd_rand(seed):
    """
    decorator for randomizing
    """
    def rand():
        """
        the seed
        """
        nonlocal seed
        seed = (1103515245*seed + 12345) & 0x7fffffff
        return seed
    return rand


rand = bsd_rand(32)


def isWinner(x, nums):
    """
    Return winner from  the game
    """
    if x <= 0 or x > 10000:
        return None
    players_dict = {'Maria': 0, 'Ben': 0}
    players = ['Maria', 'Ben']
    players_dict_winner = {'Maria': 0, 'Ben': 0}
    if x == len(nums):
        for number in nums:
            consecutive_int = [i for i in range(1, number + 1)]
            recursive_play(players[:], players_dict, consecutive_int)
            maria_wins = players_dict['Maria']
            ben_wins = players_dict['Ben']
            if maria_wins == 1:
                players_dict_winner['Maria'] += 1
            if ben_wins == 1:
                players_dict_winner['Ben'] += 1
    else:
        while x != 0:
            for number in nums:
                consecutive_int = [i for i in range(1, number + 1)]
                recursive_play(players[:], players_dict, consecutive_int)
                maria_wins = players_dict['Maria']
                ben_wins = players_dict['Ben']
                if maria_wins == 1:
                    players_dict_winner['Maria'] += 1
                if ben_wins == 1:
                    players_dict_winner['Ben'] += 1
            x -= 1
    if players_dict_winner['Maria'] == players_dict_winner['Ben']:
        winner = None
    elif players_dict_winner['Maria'] > players_dict_winner['Ben']:
        winner = 'Maria'
    else:
        winner = 'Ben'
    return winner


def recursive_play(players, players_dict, consecutive_int):
    """
    recursive helper function on the game
    """
    if len(consecutive_int) == 0:
        return
    toggle_player(players, players_dict)
    prime_numbers = []
    for number in consecutive_int:
        if check_prime(number):
            prime_numbers.append(number)
    if len(prime_numbers) == 0:
        toggle_player(players, players_dict)
        return
    prime_pick = prime_numbers[rand() % len(prime_numbers)]
    consecutive_int.remove(prime_pick)
    for number in consecutive_int[:]:
        if number % prime_pick == 0 and number in consecutive_int:
            consecutive_int.remove(number)
    recursive_play(players, players_dict, consecutive_int)


def check_prime(number):
    """check's if number is prime or not"""
    if number == 1:
        return False
    primes = [2, 3, 5, 7]
    for p in primes:
        if number % p == 0 and p != number:
            return False
    return True


def toggle_player(players, players_dict):
    """
    toggle current player
    """
    player = players.pop(0)
    players_dict[player] = 1
    players_dict[players[-1]] = 0
    players.append(player)
