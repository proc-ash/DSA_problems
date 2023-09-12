def maxDepth(s:str) -> int:
    # Write your code here.
    depth_count = 0
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
        if count > depth_count:
            depth_count = count
    return depth_count
    
if __name__ =='__main__':
    s = '((0-9))(1-3)(((4+5)((0/2)(5-1)(5/9))(9-0)((4/3)(2+7))(3-6)(((6+2)))))'
    print(maxDepth(s))
    
