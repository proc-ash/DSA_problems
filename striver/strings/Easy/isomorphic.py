def isomorph(str1, str2):
    map1, map2 ={},{}
    for c1, c2 in zip(str1, str2):
        if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1):
            return False
        map1[c1] = c2
        map2[c2] = c1
    return True
if __name__ == '__main__':
    str1 = 'add'
    str2 = 'frr'
    print(isomorph(str1, str2))
    