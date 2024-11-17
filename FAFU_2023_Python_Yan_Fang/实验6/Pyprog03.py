FACTOR =(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
CODE_TABLE=('1','0','x','9','8','7','6','5','4','3','2')
num=input()
try:
    assert len(num)==18,"身份证号码长度必须为18位"
    for i in num[:-1]:
        assert i.isdigit() or i.lower()=='x',"身份证号码必须有数字或X组成"
    if num[-1].lower() !='x':
        assert num[-1].isdigit(),"x不在最后一位"
    m=int(num[10:12])
    d=int(num[12:14])
    assert 1<=m<=12,"月份不正确"
    assert 1<=d<=31,"日期不正确"
    t=sum(int(num[i])*FACTOR[i] for i in range(17))%11
    assert num[-1].lower()==CODE_TABLE[t],"校验码不正确"
    print("身份证号码{}是正确的".format(num))
except AssertionError as t:
    print(t)
