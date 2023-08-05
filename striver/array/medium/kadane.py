# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

def kadane(array):
    max_sum = float('-inf')
    cumulative_sum = 0

    for i in range(len(array)):
        cumulative_sum += array[i]

        if cumulative_sum > max_sum:
            max_sum = cumulative_sum
        if cumulative_sum < 0:
            cumulative_sum= 0
    return max_sum

if __name__ == '__main__':
    array = [-2,1,-3,4,-1,2,1,-5,4]
    print(kadane(array))
