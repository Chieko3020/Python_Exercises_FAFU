import math
def calculate_triangle_area(a, b, c)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
def validate_positive_integer(side):
    try:
        if int(side) <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("输入的数据{}不是正整数".format(side))
def m():
    try:
        sides = input().split()
        if len(sides) != 3:
            raise IndexError("输入的边数是{}不等于3".format(len(sides)))
        for side in sides:
            validate_positive_integer(side)
        a, b, c = map(int, sides)
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("输入的数据{},{},{} 无法构成三角形".format(a, b, c))
        area = calculate_triangle_area(a, b, c)
        print("三角形的面积是{:.2f}".format(area))
    except IndexError as e:
        print("{}".format(e))
    except ValueError as e:
        print("{}".format(e))
m()
