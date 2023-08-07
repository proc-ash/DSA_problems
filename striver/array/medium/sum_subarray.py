# Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.
# A subarray is a contiguous non-empty sequence of elements within an array.

def subarraySum(array, k):
    prefix_sum = 0
    result = 0
    d = {0:1}
    for element in array:
       prefix_sum += element

       if prefix_sum -k in d:
           result += d[prefix_sum-k]

       if prefix_sum not in d:
           d[prefix_sum] = 1
       else:
           d[prefix_sum] += 1
    return result 
if __name__ == '__main__':
    array = [-1,-1,1]
    print(subarraySum(array, 0))