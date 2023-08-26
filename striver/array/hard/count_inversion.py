# Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).

# What is an inversion of an array? Definition: for all i & j < size of array, if i < j 
# then you have to find pair (A[i],A[j]) such that A[j] < A[i].

def countInversion(a, n):
    count = 0
    i,j = 0, n-1
    while i <j:
        if a[i] > a[j]:
            count += 1
        if j == i +1:
            i += 1
            j = n
        j -= 1
    return count

if __name__ =='__main__':
    array = [1,-1,1,2]
    print(countInversion(array, len(array)))