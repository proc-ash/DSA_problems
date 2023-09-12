# You are given a string num, representing a large integer. 
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num, 
# or an empty string "" if no odd integer exists.

def largestOddNumber(num):
    if int(num)%2 != 0:
        return num
    else:
        max_ele=0
        while len(num) >= 2:
            first_half = int(num[:-1])
            second_half = int(num[-1])
            if first_half % 2 !=0:
                max_ele=max(first_half, max_ele)
            if second_half % 2 !=0:
                max_ele=max(second_half, max_ele)
            num = num[:-1] 
        return max_ele if max_ele != 0 else ""

if __name__=='__main__':
    num = '3691669784801845146'
    # print(num.rstrip())
    print(largestOddNumber(num))


