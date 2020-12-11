def rec_coin(target, coins):
    # default value set to target
    min_coins = target

    # check if target in value list
    if target in coins:
        return 1
    else:
        # for every coin value less than or equal to my target
        for i in [c for c in coins if c <= target]:
            # add a coin count + recurive call
            num_coins = 1+rec_coin(target-i, coins)

            if(num_coins) < min_coins:
                min_coins = num_coins

    return min_coins


def rec_coin_dynamic(target, coins, known_result):
    # default output to target
    min_coins = target

    # Base case
    if target in coins:
        known_result[target] = 1
        return 1

    # return a known result if it happens to greater than 1
    elif known_result[target] > 0:
        return known_result[target]
    else:

        for i in [c for c in coins if c <= target]:
            num_coins = 1+rec_coin_dynamic(target-i, coins, known_result)

            if num_coins < min_coins:
                min_coins = num_coins

                known_result[target] = min_coins
    return min_coins


#print(rec_coin(63, [1, 5, 10, 25]))
target = 63
coins = [1, 5, 10, 25]
known_result = [0]*(target+1)
print(rec_coin_dynamic(target, coins, known_result))
