                       ### 请在此两行之间###    
### 你的代码写在这里
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My name is {self.name}, age is {self.age}, id is {ID}")
ID=0




###################
        
name=input()
stu=[]
while name !=  'q'  and  name  != 'Q' :
    ID+=1
    age=eval(input())
    a=Student (name,age)
    a.info()
    stu.append(a)
    name=input().strip()


