# Pattern – 12: Number Crown Pattern
# 1          1
# 12        21
# 123      321
# 1234    4321
# 12345  54321
# 123456654321

n = int(input('enter the number: '))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end='')
    for k in range(1,2*(n-1) ):
        print(' ',end='')
    for j in reversed(range(1, i+1)):
        print(j, end='')
    print('')
