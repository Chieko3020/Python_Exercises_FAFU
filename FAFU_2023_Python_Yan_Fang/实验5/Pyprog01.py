file=open('E:/Suzune/Dev/py/实验5/Pyprog01.txt','r+')
a=input()
b=input()
c=file.read()
c=c.lower()
if a>b:
    a,b=b,a
cnt=0
for char in c:
        if a<=char<=b:
            cnt+=1

print(f"The number of characters between {a} and {b} in file is {cnt}.")
file.close()
