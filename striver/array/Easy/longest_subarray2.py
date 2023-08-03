
def longestSubarray(array, k):
    max_length = 0
    element_sum = 0
    pre_sum = {}

    for i in range(len(array)):
        element_sum += array[i]

        if element_sum == k:
            max_length = max(max_length, i+1)
        
        rem = element_sum -k

        if rem in pre_sum:
            length = i - pre_sum[rem]
            max_length = max(max_length, length)
        if rem not in pre_sum:
            pre_sum[rem] = i
    return max_length

if __name__ == '__main__':
    array = [-1,1,1]
    k = 1
    print(longestSubarray(array, k))