import math  
### 请在此两行之间###    
### 你的代码写在这里
class Shape:
    def __init__(self,sName):
        self.sName=sName
class Rectangle(Shape):
    def __init__(self,sName,width,length):
        super().__init__(sName)
        self.length=length
        self.width=width
    def getArea(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,sName,radius):
        super().__init__(sName)
        self.radius=radius
    def getArea(self):
        return math.pi*(self.radius**2)




###################
    
try:
    name=input()
    s = input() .split()
    if len(s)==2:
        w,h =map(eval,s)
        r1 = Rectangle(name,w,h)
        print("The  area of Recangle {} is {:.2f}".format(r1.sName,r1.getArea()))
    elif len(s)==1:  
        r = eval(s[0])
        c1 = Circle(name,r)
        print("The  area of Circle {} is {:.2f}" .format (c1.sName,c1.getArea()))
    else:
        print("输入边个数有误！")
except:
    print("程序出错")
