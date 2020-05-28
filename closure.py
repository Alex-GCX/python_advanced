def line(a, b):
    num = 1

    def cal(c):
        nonlocal num
        num = 0
        return a + b + c + num
    return cal


print('------line1---------')
line1 = line(1, 2)
print(line1(3))
print(line1(4))
print(line1(5))
print('--------line2---------')
line2 = line(2, 3)
print(line2(10))
print(line2(20))
print(line2(30))
