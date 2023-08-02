# Problem Statement: You are given an array of integers, your task is to move all the zeros 
# in the array to the end of the array and move non-negative integers to the front by maintaining their order.

def moveToEnd(array):
    zero_index = -1
    index = 0
    while index < len(array):
        if array[index] == 0:
            zero_index = index
            break
        index += 1
    
    if zero_index == -1:
        return array

    for index in range(zero_index+1, len(array)):
        if array[index] != 0:
            array[index], array[zero_index] = array[zero_index], array[index]
            zero_index += 1
    return array

if __name__ == '__main__':
    array = [-1,0,-2,4,0,-3,5]

    print(moveToEnd(array))