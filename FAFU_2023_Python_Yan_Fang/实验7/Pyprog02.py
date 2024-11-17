import math
### 请在此两行之间###    
### 你的代码写在这里
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def get_area(self):
        p=(self.a+self.b+self.c)/2
        s=math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return s
    def get_cal(self):
        C=self.a+self.b+self.c
        return C




###################

try:
    a = float ( input ())
    b = float ( input ())
    c = float ( input ())
    if a >0 and b >0 and c >0 and a+b > c and a + c > b and b + c > a :
        triangle = Triangle ( a , b ,c )
        print ("The perimeter is {:.2f}. The area is {:.2f}.". format ( triangle . get_cal(), triangle . get_area ()))
    else :
        print ("不能构成三角形！")
except:
    print("输入有误！")
