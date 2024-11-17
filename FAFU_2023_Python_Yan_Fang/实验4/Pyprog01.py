### 请在此两行之间编写函数Even ###
### 你的代码写在这里
def Even(i):
    if(i%2==0):
        return True
    else:
        return False

### 请在此两行之间编写函数Even ###

strdata=input()
sum=0
for item in strdata.split():
    i=int(item)
    if Even(i)==False: sum=sum+i
print(sum)
