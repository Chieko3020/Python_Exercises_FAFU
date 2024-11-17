### 请在此两行之间###    
### 你的代码写在这里
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"Point({self.x},{self.y})"
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return Point(x,y)
    def __mul__(self,n):
        x=self.x*n
        y=self.y*n
        return Point(x,y)
    def __truediv__(self,n):
        x=self.x/n
        y=self.y/n
        return Point(x,y)
    




###################
try:
    x1,y1=map(eval,input().split())
    x2,y2=map(eval,input().split())
    n=eval(input())
    a =Point (x1,y1)
    b =Point (x2,y2)
    #输出结果都为Point对象
    print (a+ b)
    print (a - b)
    print (a *n)
    print (a /n)
except:
    print("你的输入有误")
