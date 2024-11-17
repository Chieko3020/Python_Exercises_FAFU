def isprime(min,max):
    ans=0
    for i in range(min,max):
        cnt=0
        for j in range(2,i):
            if(i%j==0):
                cnt=cnt+1
        if (cnt==0):
            ans=ans+1
    return ans
m,n=eval(input())
print(isprime(m,n))

