import re
import strin
a=input()
pu=string.punctuation
a=re.sub('[{}]'.format(pu),"",a)
dic={}
a=a.lower()
ls=a.split()
for i in ls:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
cnt=len(dic)
print("There are",cnt,"words in the paragraph.")
