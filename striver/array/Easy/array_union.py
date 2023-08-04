# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

def arrayUnion(arr1, arr2):

    i = 0
    j = 0
    union = []
    while i <len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        union.append(arr2[j])
        j += 1

    return union

if __name__ == '__main__':
    arr1 = [-3,-2,0,5,7]
    arr2 = [-1,1,2,3,4,6]

    print(arrayUnion(arr1, arr2))