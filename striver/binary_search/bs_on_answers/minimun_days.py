# Problem Statement: You are given ‘N’ roses and you are also given an array ‘arr’  
# where ‘arr[i]’  denotes that the ‘ith’ rose will bloom on the ‘arr[i]th’ day.
# You can only pick already bloomed roses that are adjacent to make a bouquet. 
# You are also told that you require exactly ‘k’ adjacent bloomed roses to make a single bouquet.
# Find the minimum number of days required to make at least ‘m’ bouquets each containing ‘k’ roses. 
# Return -1 if it is not possible.

def bouqetsMade(arr, day, r, b):
    count = 0
    no_of_bouqets = 0

    for i in range(len(arr)):
        if arr[i]<= day:
            count += 1
        else:
            no_of_bouqets += count // r
            count = 0
    no_of_bouqets += count // r
    return no_of_bouqets >= b

def roseGarden(arr, r, b):
    # write yur code here
    total_roses = r*b
    if len(arr)<total_roses:
        return -1
    
    low = min(arr)
    high = max(arr)
    while low <= high:
        mid = (low + high)//2

        if bouqetsMade(arr, mid ,r ,b):
            high = mid -1
        else:
            low = mid + 1
    return low

if __name__ =='__main__':
    arr = [7,7,7,7,13,11,12,7]
    r = 2
    b = 3
    print(roseGarden(arr, r, b))