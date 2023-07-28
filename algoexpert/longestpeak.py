# write a function that returns longest peak of an integer array

def longestPeak(array):
    element_index = 1
    longest_peak = 0
    while element_index < len(array) - 1:
        if array[element_index - 1] < array[element_index] > array[element_index + 1]:
            left_index = element_index - 1
            while left_index > 0 and array[left_index] > array[left_index -1]:
                left_index -= 1
            right_index = element_index +1
            print(f"ri: {right_index}")
            while right_index < len(array) - 1 and array[right_index] > array[right_index + 1]:
                right_index += 1
            print(f"ria: {right_index}")
        else:
            element_index += 1
            continue

        current_peak = right_index - left_index + 1
        #print(current_peak)
        longest_peak = max(longest_peak, current_peak)
        element_index = right_index
    return longest_peak
    

if __name__ == '__main__':
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(array))