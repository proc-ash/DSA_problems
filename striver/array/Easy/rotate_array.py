# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

def reverse(array, start, end):
    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
def rotateKPlace(array,k,direction):
    if direction == 'right':
        #reversing first n-k elements
        
        reverse(array,0, len(array)-k)

        # reversing last k elements

        reverse(array, len(array)-k,len(array) - 1)

        #reversing whole array
        reverse(array, 0, len(array) - 1)

    if direction == 'left':
        #reversing first n-k elements
        
        reverse(array,0, k - 1)

        # reversing last k elements

        reverse(array, k, len(array) - 1)

        #reversing whole array
        reverse(array, 0, len(array) - 1)
    return array
    
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    print(rotateKPlace(array,2, 'right'))
    
