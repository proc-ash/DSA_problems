#write a function that takes an input array and a targetsum. return any two number that sum up to target

def twoNumbersum(array, targetSum):
    check_dict ={}
    for element in array:
        if targetSum - element not in check_dict.keys():
            check_dict[element] = True
        else:
            return [targetSum, element]
    return []

if __name__ == "__main__":
    array= [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumbersum(array, targetSum))

