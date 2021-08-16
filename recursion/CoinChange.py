# def coin_change(target, coins):
#     min_coins = target

#     if target in coins:
#         return 1
    

#     else:

#         # for every coin value that is <= than target
#         for i in [c for c in coins if c <= target][::-1]:

#             #Recursive Call (add a count coin and subtract from the target)
#             num_coins = 1 + coin_change(target-i, coins)

#             # Reset Minimum if we have a new minimum
#             if num_coins < min_coins:
#                 min_coins = num_coins

#     return min_coins

# print(coin_change(3, [1, 5, 10,25]))

# coins = [1, 5, 10]
# target = 8

# for i in [c for c in coins if c <= target]:
#     print(i)

# def rec_coin_dynam(target, coins, known_results):

#     # Default output to target
#     min_coins = target

#     # Base Case
#     if target in coins:
#         known_results[target] = 1
#         return 1

#     # Return a known result if it happens to be greater than 1
#     elif known_results[target] > 0:
#         return known_results[target]

#     else:

#         # For every coin value that is <= target
#         for i in [c for c in coins if c<=target]:
#             num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)

#             if num_coins < min_coins:
#                 min_coins = num_coins

#                 #Reset that known result
#                 known_results[target] = min_coins

#     return min_coins

# target = 63
# coins = [1, 5, 10,25]
# known_results = [0]*(target+1)
# print(rec_coin_dynam(target, coins, known_results))

coins = [1, 5, 10,25]

print(coins[2])