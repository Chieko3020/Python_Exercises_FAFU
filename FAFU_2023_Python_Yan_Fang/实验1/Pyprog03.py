a=int(input())
n=1
s=0
for i in range(1,a+1):
    if((i%3==0)and(i%7!=0)):
            s=s+i

print(s)
    

