# Problem Statement: You are given an array of integers ‘arr’ and an integer 
# i.e. a threshold value ‘limit’. Your task is to find the smallest positive integer divisor, 
# such that upon dividing all the elements of the given array by it, 
# the sum of the division’s result is less than or equal to the given threshold value.
from math import *
def findDvisor(arr, div):
    div_sum = 0
    for i in range(len(arr)):
        div_sum += ceil(arr[i]/div)
    return div_sum

def smallestDivisor(arr: [int], limit: int) -> int:
    # Write your code here.

    low = 1
    high = max(arr)

    while low <= high:
        mid = (low + high)//2
        if findDvisor(arr, mid) <= limit:
            high = mid -1
        else:
            low = mid +1 
    return low

if __name__ =='__main__':
    arr = [8,4,2,3]
    limit = 6
    print(smallestDivisor(arr, limit))