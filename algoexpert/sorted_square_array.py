#given an non-empty array sorted in ascendn=ing order write 
#a function returns square of array sorted in ascending order

def soertedSquaredArray(array):
    result = [0]*len(array)
    left_index = 0
    right_index = len(array) - 1
    assign_index = right_index 
    while left_index <= right_index:
        if array[left_index]**2 > array[right_index]**2:
            result[assign_index] = array[left_index] **2
            left_index +=1
        else:
            result[assign_index] = array[right_index] **2
            right_index -=1
        assign_index -= 1
    return result

if __name__ == '__main__':
    array = [-3, -2, 1, 3, 6, 8]
    print(soertedSquaredArray(array))