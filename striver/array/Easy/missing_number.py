# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
# Find the number(between 1 to N), that is not present in the given array.

def missingNumber(array,n):
    array_sum = sum(array)
    actual_sum = (n * (n+1) ) / 2

    return int(actual_sum - array_sum)

if __name__ == '__main__':
    array = [1,2,3,4]

    print(missingNumber(array, 5))

