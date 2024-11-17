try:
    A=eval(input())
    a=20/A
except ZeroDivisionError as c:
    print("The divisor cannot be 0:{}".format(c))
except NameError as e:
    print("The input is not a number:{}".format(e))
else:
    print("{:.2f}".format(a))
