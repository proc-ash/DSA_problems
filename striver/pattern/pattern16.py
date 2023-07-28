# Pattern – 16: Alpha-Ramp Pattern
# A 
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F

n = int(input('number: '))
start = 65

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(start),end=' ')
    start +=1
    print('')