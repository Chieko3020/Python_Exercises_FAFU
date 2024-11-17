import os
###请在此两行之间按题目要求编写代码，不得删改上面代码，否则不得分############################
n = int(input())
with open("Pyprog03.csv","w") as file:
    file.write("姓名,联系电话\n")
    for i in range(n):
        inf=input().split()
        name,tel=inf[0],inf[1]
        file.write(f"{name},{tel}\n")
###请在此两行之间按题目要求编写代码，不得删改下面代码，否则不得分############################
if os.path.exists('Pyprog03.in') and os.path.isfile('Pyprog03.in'):
    if os.path.exists('Pyprog03.csv'):
        filename03=open('Pyprog03.csv', 'r')
        print(filename03.read())
        filename03.close()
