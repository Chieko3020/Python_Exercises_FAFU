import os
d=input().strip()
t=input().strip()
if not os.path.exists(d):
    print("该目录不存在")
else:
    for root,dirs,files in os.walk(d):
        for f in files:
            if t in f:
                fp=os.path.relpath(os.path.join(root,f),d)
                print(os.path.join(d,fp))
