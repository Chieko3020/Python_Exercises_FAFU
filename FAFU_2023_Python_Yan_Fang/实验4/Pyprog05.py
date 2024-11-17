### 请在此两行之间编写函数isPrime和函数Reverse ### 
### 你的代码写在这里
import string
def kinds_of_char(i):
    d=0
    l=0
    u=0
    p=0
    if len(i)<8:
        print("弱密码")
    else:
        for c in i:
            if c in string.digits:
                d=1
            elif c in string.ascii_lowercase:
                l=1
            elif c in string.ascii_uppercase:
                u=1
            elif c in string.punctuation:
                p=1
        if d+l+u+p==1:
            print("弱密码")
        if d+l+u+p==2:
            print("中等强度密码")
        elif d+l+u+p==3:
            print("强密码")
        elif d+l+u+p==4:
            print("极强密码")
### 请在此两行之间编写函数kinds_of_char ### 
pwd = input()
kinds_of_char(pwd)
