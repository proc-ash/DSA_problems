# insertion sort

def insertionSOrt(array):
    for i in range(0, len(array)-1):
        for j in range(i+1,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

if __name__ == '__main__':
    array = [7,5,1,6,4,9,2]

    insertionSOrt(array)
    print(array)
