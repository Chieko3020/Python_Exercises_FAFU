a,b,c=eval(input())
if (a+b>c)and(a+c>b)and(b+c>a):
    p=(a+b+c)/2
    s=pow((p*(p-a)*(p-b)*(p-c)),0.5)
    print("{:.2f}".format(s),"{:.2f}".format(p*2))
else:
    print("Not a Valid Triangle")



