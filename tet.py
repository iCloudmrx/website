n=int(input())
s=input().split(' ')
massive=[]
for i in s:
    massive.append(int(i))
sum1=0
while len(massive)!=0:
    sum1+=max(massive)
    del massive[massive.index(max(massive))]
    if len(massive)!=0:
        del massive[massive.index(max(massive))]
print(sum1)