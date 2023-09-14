# Problem Statement: You are the owner of a Shipment company. 
# You use conveyor belts to ship packages from one port to another. 
# The packages must be shipped within ‘d’ days.
# The weights of the packages are given in an array ‘of weights’. 
# The packages are loaded on the conveyor belts every day in the same order as they appear in the array. 
# The loaded weights must not exceed the maximum weight capacity of the ship.
# Find out the least-weight capacity so that you can ship all the packages within ‘d’ days.

def findDays(weights, cpacity):
    loads = 0
    day = 1
    for i in range(len(weights)):
        if loads + weights[i] > cpacity:
            day += 1
            loads = weights[i]
            print('if',day,loads)
        else:
            loads += weights[i]
            print('else: ',loads,day)
    print('final',day)
    return day

def leastWeightCapacity(weights, d):
    # Write your code here.
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high)//2
        print(f'mid: {mid}')
        noOfDays = findDays(weights,mid)
        if noOfDays <= d:
            high = mid -1
        else:
            low = mid + 1
    return low

if __name__=='__main__':
    arr = [5,4,5,2,3,4,5,6]
    d = 5
    print(leastWeightCapacity(arr, d))