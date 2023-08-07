# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest
# sequence which contains the consecutive elements.

#approach: by sorting the array

def longestConsecutiveSequence(array):
    array.sort()
    # sequence = []
    count = 0
    longest = 1
    prev_element = float('-inf')
    for current_element in range(len(array)):
        if array[current_element] - 1 == prev_element:
            count += 1
            prev_element = array[current_element]
        elif array[current_element] != prev_element:
            prev_element = array[current_element]
            count = 1
        longest = max(longest, count)
    return longest
if __name__ == '__main__':
    array = [100, 200, 1, 3, 2, 4]
    print(longestConsecutiveSequence(array))