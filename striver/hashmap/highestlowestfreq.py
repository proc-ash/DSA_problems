# Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

def highLowFreq(array):
    array_map = {}

    for element in array:
        if element not in array_map.keys():
            array_map[element] = 1
        else:
            array_map[element] += 1

    sorted(array_map, key=lambda key: array_map[key])
    min_freq = list(array_map.keys())[0]
    max_freq = list(array_map.keys())[-1]

    return min_freq, max_freq

if __name__ == '__main__':
    array = [10,5,10,15,10,5]
    print(highLowFreq(array))