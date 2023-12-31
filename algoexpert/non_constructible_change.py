# We are given an array of positive integers, which represent the values of coins that we have in our possession. 
# The array could have duplicates. We are asked to write a function that returns the minimum amount of change that 
# we cannot create with our coins. For instance, if the input array is [1, 2, 5],
# the minimum amount of change that we cannot create is 4, since we can create 1, 2, 3 (1 + 2) and 5.

def nonConstuctibleChanges(coins):
    coins.sort()
    minimum_change = 0
    for coin in coins:
       if coin > minimum_change+1:
          return minimum_change+1
       minimum_change += coin
    return minimum_change +1

if __name__ == '__main__':
   coins = [6, 4, 5, 1, 1, 8, 9]
   print(nonConstuctibleChanges(coins))
