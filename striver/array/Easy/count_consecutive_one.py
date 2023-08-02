# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

def countConsecutiveOne(array):
    consecutive_one = 0
    temp_count = 0
    for i in range(len(array)):
        if array[i] == 1:
            temp_count += 1
        else:
            consecutive_one = max(consecutive_one, temp_count)
            temp_count = 0
        consecutive_one = max(consecutive_one, temp_count)
    return consecutive_one

if __name__ == '__main__':
    array = [1,1,1,1,0,1,1,1]
    print(countConsecutiveOne(array))