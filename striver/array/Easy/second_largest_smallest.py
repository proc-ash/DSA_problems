# Problem Statement: Given an array, find the second smallest and second largest element in the array. 
# Print ‘-1’ in the event that either of them doesn’t exist.

def secondSmallest(array):
    if len(array)< 2:
        return -1
    small = float('inf')
    second_small = float('inf')
    for element in array:
        if element < small:
            second_small = small
            small = element
        elif element < second_small and element != small:
            second_small = element
    return second_small

def secondLargest(array):
    if len(array) < 2:
        return -1
    large = float('-inf')
    second_large = float('-inf')

    for element in array:
        if element > large:
            second_large = large
            large = element
        elif element > second_large and element != large:
            second_large = element
    return second_large    
if __name__ == '__main__':
    array = [7,6,1,5,4,9,2]

    print(secondSmallest(array))
    print(secondLargest(array))