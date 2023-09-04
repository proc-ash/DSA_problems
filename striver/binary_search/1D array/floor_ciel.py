# Problem Statement: You’re given an sorted array arr of n integers and an integer x.
# Find the floor and ceiling of x in arr[0..n-1].
# The floor of x is the largest element in the array which is smaller than or equal to x.
# The ceiling of x is the smallest element in the array greater than or equal to x.

def ceilingInSortedArray(n, x, arr):
    # Write your code here.
    ceiling=float("inf")
    floor=-1

    for i in arr:

        if i==x:
            ceiling=i
            floor=i
            break
        if i<x and i>floor:
            floor=i
        if i>x and i<ceiling:
            ceiling=i
    
    if ceiling==float("inf"):
        ceiling=-1

    convert_to_str = lambda x: str(x)
    result_string = ' '.join(map(convert_to_str, [floor,ceiling]))

    return result_string
