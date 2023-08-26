# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

def maxProductSubarray(nums):
    n= len(nums)
    pre = 1
    suff = 1
    ans = float('-inf')
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= nums[i]
        suff *= nums[n-i-1]
        ans = max(ans, max(pre, suff))
    return ans


if __name__ == '__main__':
    nums = [-2,3,-4,0]
    print(maxProductSubarray(nums))
