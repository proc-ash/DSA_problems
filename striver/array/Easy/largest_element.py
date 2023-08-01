# Problem Statement: Given an array, we have to find the largest element in the array.

def largestElement(array):
    largest_element = 0
    for element in array:
        largest_element = max(largest_element,element)
    return largest_element

if __name__ == '__main__':
    array = [7,6,1,5,4,9,2]
    print(largestElement(array))
    
