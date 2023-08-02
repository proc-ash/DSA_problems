# liner search

def linearSearch(array, find):
    for element in array:
        if element == find:
            return find
    return -1

if __name__ == '__main__':
    array = [3,5,-2,7,89,-4,0]
    print(linearSearch(array,1))