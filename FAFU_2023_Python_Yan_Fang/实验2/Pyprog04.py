import random
m=int(input())
n=int(input())
random.seed(m)
list=[]
for i in range (1,n+1):
    list.append(random.randint(1,100))
list.sort()
print(list)
cnt=0;
for j in range(0,len(list)):
    if(list[j]%2==0):
        cnt=cnt+1
print(cnt)
