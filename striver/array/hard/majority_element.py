# Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. 
# If no such element exists, return an empty vector.
def majorityElement(array):
    count1, count2 = 0,0
    ele1,ele2 = float('-inf'), float('-inf')
    for element in array:
        if count1 == 0 and element != ele2:
            count1 = 1
            ele1 = element
        elif count2 == 0 and element != ele1:
            count2 = 1
            ele2 = element
        elif element == ele1:
            count1 += 1
        elif element == ele2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    ls = []
    cnt1, cnt2 = 0,0
    for element in array:
        if element ==ele1:
            cnt1 += 1
        if element ==ele2:
            cnt2 += 1
    majority = int(len(array)/3) + 1
    if cnt1 >= majority:
        ls.append(ele1)
    if cnt2 >= majority:
        ls.append(ele2)
    return ls
        
if __name__ =='__main__':
    array = [4,4,2,4,3,4,4,3,2,4]
    print(*majorityElement(array))