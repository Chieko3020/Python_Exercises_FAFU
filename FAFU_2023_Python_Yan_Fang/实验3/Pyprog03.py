import random
p, s=eval(input()
cnt=0
a=int(p/10)
random.seed(s)
while(p>0):
    p-=random.randint(0,a)
    cnt=cnt+1
print(cnt)
