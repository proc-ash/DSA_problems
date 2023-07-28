# Pattern – 10: Half Diamond Star Pattern
#   *  
#   **
#   ***  
#   **
#   *  
n = int(input('number: '))
for i in range(n+1):
    print('*'*i)
for i in range(n-1,0,-1):
    print('*'*i)
