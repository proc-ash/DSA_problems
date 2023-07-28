# Pattern-18: Alpha-Triangle Pattern
# F
# E F
# D E F
# C D E F
# B C D E F
# A B C D E F
n = int(input('number: '))
start  = 65 + n -1
for i in range(1, n+1):
    start = 65 + n - i
    for j in range(1,i+1):
        print(chr(start),end=' ')
        start +=1 
    print('')