# insertion sort using recursion
def insertionSort(array, n):
    if n == len(array) - 1:
        return

    for j in range(n+1, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
    
    insertionSort(array,n+1)

if __name__ == '__main__':
    array = [7,5,1,6,4,9,2]

    insertionSort(array,0)
    print(array)
