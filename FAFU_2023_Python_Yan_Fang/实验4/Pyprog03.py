### 请在此两行之间编写函数isPrime和函数Reverse ### 
### 你的代码写在这里
def Ack(m,n):
    if(m==0):
        return n+1
    elif(n==0 and m>0):
        return Ack(m-1,1)
    elif(m>0 and n>0):
        return Ack(m-1,Ack(m,n-1))

        
### 请在此两行之间编写函数isPrime和函数Reverse ### 
m,n=map(int,input().split())
print(Ack(m,n))
