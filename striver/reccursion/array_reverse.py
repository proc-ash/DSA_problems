# Problem Statement: You are given an array. The task is to reverse the array and print it. 
from typing import *
def arrayReverse(n, nums):
    if n == 0:
        return 0
    return nums[n-1] + arrayReverse(n-1, nums) 
if __name__=='_main__':
    n=5
    nums = [7,5,3,2,1]
    print(arrayReverse(n,nums))