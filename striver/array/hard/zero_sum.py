# Problem Statement: Given an array containing both positive and negative integers, 
# we have to find the length of the longest subarray with the sum of all elements equal to zero.

def longestSubarray(array):
    max_length = 0
    sub_len = {}
    sum = 0
    for i in range(len(array)):
        sum += array[i]
        if sum == 0:
            max_length = i + 1
        else:
            if sum in sub_len:
                max_length = max(max_length,i - sub_len[sum])
            else:
                sub_len[sum] = i
    return max_length

if __name__ == '__main__':
    array = [9,-3,3,-1,6,-5]
    print(longestSubarray(array))