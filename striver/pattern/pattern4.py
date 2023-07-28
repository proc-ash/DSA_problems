#Pattern – 4: Right-Angled Number Pyramid – II
# 1
# 2 2
# 3 3 3
# 4 4 4 4 
# 5 5 5 5 5
n = int(input('Enter the number: '))

for i in range(1, n+1):
    print(str(i)*i)