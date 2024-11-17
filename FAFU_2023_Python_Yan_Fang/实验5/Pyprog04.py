import os
###请在此两行之间按题目要求编写代码，不得删改上面代码，否则不得分############################
import csv,re
from collections import Counter
a=input()
s=re.findall(r'\w+',a.lower())
c=Counter(s)
t=c.most_common(3)
with open("Pyprog04.csv","w",newline='') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(["单词","次数"])
    for w,c in t:
        csv_writer.writerow([w,c])



###请在此两行之间按题目要求编写代码，不得删改下面代码，否则不得分############################
if os.path.exists('Pyprog04.in') and os.path.isfile('Pyprog04.in'):
    if os.path.exists('Pyprog04.csv'):
        filename04=open('Pyprog04.csv', 'r')
        print(filename04.read())
        filename04.close()
