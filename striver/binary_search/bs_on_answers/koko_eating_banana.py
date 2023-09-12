import math
def totalHour(piles, hourly):
    total_hour = 0
    for i in range(len(piles)):
        total_hour += math.ceil(piles[i]/hourly)
    return total_hour
def minimumBananaEating(piles, hour):
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low + high)//2
        if totalHour(piles, mid) <= hour:
            high = mid -1
        else:
            low = mid +1
    return low

if __name__ == '__main__':
    piles = [30,11,23,4,20]
    hour = 6
    print(minimumBananaEating(piles, hour))