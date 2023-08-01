# Problem Statement: Given an integer array sorted in non-decreasing order, 
# remove the duplicates in place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. 
# It does not matter what you leave beyond the first k elements.

# Note: Return k after placing the final result in the first k slots of the array.

def removeDuplicate(array):
    i = 0
    for j in range(1,len(array)):
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]
    return i + 1 

if __name__ == '__main__':
    array = [1,1,2,6,6,7,9]

    print(array[:removeDuplicate(array)])