nList=eval(input())
num=int(input())
x=int(input())
l=len(nList)
if(nList.count(num)==0):
    nList.append(x)
else:
    nList.insert(nList.index(num)+1,x)
print(nList)
        
