### 请在此两行之间编写函数Gcd ###    
### 你的代码写在这里
def Gcd(x,y):
    temp=y;
    while(x%y!=0):
        temp=x%y
        x=y
        y=temp
    return temp;


### 请在此两行之间编写函数Gcd ###
m=int(input())
n=int(input())
print(int(m*n/Gcd(m,n)))
