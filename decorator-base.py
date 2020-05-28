def set_func(func):
    def cal_func():
        print('--------进行数据验证-------')
        print('此时变量func指向:', func)
        func()
    return cal_func


def test1():
    print('-------调用了test1--------')


@set_func
def test2():
    print('-------调用了test2--------')


print('装饰前,test1指向:', test1)
print('手动实现装饰器:')
print('1.新建变量ret接收set_func的返回值')
ret = set_func(test1)
print('2.此时ret指向:', ret)
print('3.调用ret')
ret()
print('=' * 30, '我是分割线', '=' * 30)
print('1.将上述ret变量名换成test1')
test1 = set_func(test1)
print('2.此时test1指向:', test1)
print('3.调用test')
test1()
print('=' * 30, '我是分割线', '=' * 30)
print('使用装饰器符号@装饰test2:')
test2()
