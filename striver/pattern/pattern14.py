# Pattern-14: Increasing Letter Triangle Pattern
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F

start = 65
n = int(input('number: '))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(start),end=' ')
        start += 1
    start = 65
    print('')