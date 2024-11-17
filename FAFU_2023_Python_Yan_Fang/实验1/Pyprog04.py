n=int(input())
a=1
b=1
i=1
while(i<=n-2):
    temp=a+b
    a=b
    b=temp
    i=i+1
print(temp)
    

