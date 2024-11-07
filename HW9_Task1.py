import timeit as tm
import random

COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    coins_needed = {}
    for coin in COINS:
        div = amount // coin
        if div > 0:
            coins_needed[coin] = div
        amount %= coin
    return coins_needed


def find_min_coins_impl(amount, memo={}):
    if amount == 0:
        return 0, {}
    if amount < 0:
        return float('inf'), {}
    if amount in memo:
        return memo[amount]

    min_coins = float('inf')
    coins_needed = {}
    for coin in COINS:
        if amount < coin:
            break
        num_coins, sub_coins_needed = find_min_coins_impl(amount - coin, memo)
        if num_coins != float('inf'):
            if num_coins + 1 < min_coins:
                min_coins = num_coins + 1
                coins_needed = sub_coins_needed.copy()
                coins_needed[coin] = coins_needed.get(coin, 0) + 1

    memo[amount] = (min_coins, coins_needed)
    return memo[amount]

def find_min_coins(amount):
    num_coins, coins_needed = find_min_coins_impl(amount)
    if num_coins == float('inf'):
        return None
    return coins_needed


def main():
    tests = [113]
    vals = sorted(random.sample(range(100, 100000), 10))
    for val in vals:
        print(f"Number of coins needed for {val}: {find_coins_greedy(val)}")
        print(f"Number of coins needed for {val}: {find_min_coins(val)}")

        tests_runs = 10000
        print(f"Greedy x{tests_runs}: {tm.timeit(lambda: find_coins_greedy(val), number=tests_runs):.6f}")
        print(f"Dynamic x{tests_runs}: {tm.timeit(lambda: find_min_coins(val), number=tests_runs):.6f}")


if __name__ == "__main__":
    main()
