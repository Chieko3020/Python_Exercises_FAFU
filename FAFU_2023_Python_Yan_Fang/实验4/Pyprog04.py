### 请在此两行之间编写函数isPrime和函数Reverse ### 
### 你的代码写在这里
def isPrime(x):
    if(x<2):
        return False
    elif(x==2):
        return True
    else:
        for i in range(2,x):
            if(x%i==0):
                return False
                break
        else:
            return True
def Reverse(x):
    x=str(x)
    a=x[::-1]
    b=int(a)
    return b






### 请在此两行之间编写函数isPrime和函数Reverse ### 
m,n=map(int,input().split())
for i in range(m, n+1):
    if isPrime(i) and isPrime(Reverse(i)) :
        print(i, end=' ')
