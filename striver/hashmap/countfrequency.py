# Problem statement: Given an array, we have found the number of occurrences of each element in the array.

def countFrequency(array):
    array_map = {}
    
    for element in array:
        if element not in array_map.keys():
            array_map[element] = 1
        else:
            array_map[element] += 1
        
    for key, value in array_map.items():
        print(f'{key} -> {value}')

if __name__ == '__main__':
    array = [10,5,10,15,10,5]
    countFrequency(array)