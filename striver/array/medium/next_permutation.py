# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given 
# array into the lexicographically next greater permutation of numbers.

# def nextPermutation(array):
#     index = -1
# # first thing is to find longest prefix match i.e. the point from where we can change the numbers and 
#     for i in range(len(array)-2,-1,-1):
#         if array[i] <array[i+1]:
#             index = i
#             break
#     #check if no prefix is found then just return the reverse of the array
#     if index == -1:
#         return array[::-1]
    
#     # after finding the prefix find the smallest greater number present in the array after the index

#     for i in range(len(array)-1,index,-1):
#         if array[i] > array[index]:
#             array[i], array[index] = array[index], array[i]
#             break
#     # now after finding that number reverse the whole array from index till end of element
#     array[index+1:] = reversed(array[index+1:])

#     return array

if __name__ =='__main__':
    array = [2, 1, 5, 4, 3, 0, 0]
    # print(nextPermutation(array))
    print(array[::-1])

