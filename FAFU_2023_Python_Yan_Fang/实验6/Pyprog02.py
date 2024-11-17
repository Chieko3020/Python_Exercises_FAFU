while(1):
    try:
        n=eval(input())
    except:
        print("",end="")
    else:
        break
num=0
q=n
try:
    while(q):
        q-=1
        x=int(input())
        num+=x
except TypeError as t:
    print(t)
except ValueError as t:
    print(t)
else:
    print("ALL OK")
    print("avg grade={:.2f}".format(num/n))
print("Process Completed")
