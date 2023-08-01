# Problem Statement: Given an array of N integers, left rotate the array by one place.

def leftRotate(array):
    temp = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = temp

    return array


if __name__ == '__main__':
    array = [1,2,4,5,6,7,9]

    print(leftRotate(array))