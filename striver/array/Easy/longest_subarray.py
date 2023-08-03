# Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
def longestSubarray(array,k):
    left, right = 0, 0
    max_length = 0
    element_sum = array[0]
    while right < len(array):
        while left <= right and element_sum >k:
            element_sum -= array[left]
            left +=1

        if element_sum == k:
            max_length = max(max_length, right - left + 1)

        right += 1
        if right < len(array):
            element_sum += array[right]      
    return max_length

if __name__ == '__main__':
    array = [-4,7,6,1,3,-5,8,2,9]
    k = 10
    print(longestSubarray(array,10))
