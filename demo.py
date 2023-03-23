from math import sqrt
n = int(input())
if n == 2:
    print('yes')
elif n<5:
    print('no')
elif n%2==0:
    print('no')
elif (sqrt(n-4)%1==0):
    print('yes')
elif (sqrt(n-1)%1==0):
    print('yes')
else:
    print('no')