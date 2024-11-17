w=float(input())
if w<=2:
    p=7.5
else:
    p=(w-2)*1.8+7.5
print("{:.1f}".format(p))