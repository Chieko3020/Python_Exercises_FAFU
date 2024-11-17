fname=open('E:/Suzune/Dev/py/实验5/Pyprog02.csv','r')
d=fname.read()
nList=[int(num)for num in d.split(",")]
n=int(input())
r=[str(num) for num in nList if num%n ==0]
print(" ".join(r))
