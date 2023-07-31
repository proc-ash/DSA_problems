# bubble sort using recursion

def bubbleSort(array, n):
    
    if n == 1:
        return
    for j in range(1,n):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j-1], array[j]
    
    bubbleSort(array,n-1)

if __name__ == '__main__':
    array = [7,6,1,5,4,9,2]
    bubbleSort(array, len(array))
    print(array)