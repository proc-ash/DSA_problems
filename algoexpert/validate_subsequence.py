# given two non-empty array of integers write a function 
# that returns whether the second array is subsequence of first array
# function(first_array, second_array)

def isValidSubsequence(array, sequence):
    second_idx = 0
    for first_idx in range(len(array)):
        if array[first_idx] == sequence[second_idx]:
            second_idx +=1
        if second_idx == len(sequence):
            return True
    return False

if __name__ == "__main__":
    first_array = [5, 1, 22, 25, 6, -1, 8, 10]
    second_array = [1, 6, -1, 10]

    print(isValidSubsequence(first_array, second_array))

