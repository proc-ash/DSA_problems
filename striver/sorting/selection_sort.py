# selection sort
# select the minimun or maximum element in the unsorted array
# after that swap it with the first or last element of the unsorted array

def getMinElement(array,start):
    min_element = start 
    for i in range(start,len(array)):
        if array[i] < array[min_element]:
            min_element = i
    return min_element
def selectionSort(array):
    for i in range(len(array)):
        first_index = i
        #print(first_index+1, len(array)-i)
        min_element = getMinElement(array, first_index)
        array[first_index], array[min_element] = array[min_element], array[first_index]
if __name__ == "__main__":
    array = [7,6,1,5,4,9,2]
    selectionSort(array)
    print(array)
