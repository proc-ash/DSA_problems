# Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

def appearOnce(array):
    array.sort()
    for i in range(0,len(array),2):
        if i == len(array)-1:
            return array[i]
        if array[i] - array[i+1] != 0:
            return array[i]
    return -1

if __name__ == '__main__':
    array = [7,2,6,5,8,2,7,6,8]
    print(appearOnce(array))