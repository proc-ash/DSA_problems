# quick sort

def partition(array, low, high):
    pivot = array[high]

    i = low -1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1

            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]

    return i+1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quicksort(array, low, pi-1)

        quicksort(array, pi +1, high)

if __name__ == '__main__':
    array = [7,6,1,5,4,9,2]

    quicksort(array, 0, len(array) - 1)
    print(array)