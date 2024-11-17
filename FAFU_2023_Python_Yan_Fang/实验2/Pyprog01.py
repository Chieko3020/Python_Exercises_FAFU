list=eval(input())
l=len(list)
s=float(sum(list[2:l:3]))
k=int(len(list[2:l:3]))
print("The average age of",k , "students is",format(s/k,'.1f'))

