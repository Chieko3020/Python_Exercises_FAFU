a=input()
num=a.split(" ")
nList=[eval(i) for i in num]
i=int(input())
nList.pop(i)
nList.sort()
nList.reverse()
print(nList)
