def set_func1(func):
    print('----1.权限验证开始装饰----')

    def cal_func(*args, **kwargs):
        print('------1.权限验证------')
        return func(args, kwargs)
    return cal_func


def set_func2(func):
    print('----2.数据验证开始装饰----')

    def cal_func(*args, **kwargs):
        print('------2.数据验证------')
        return func(args, kwargs)
    return cal_func


@set_func1
@set_func2
def test1(para, *args, **kwargs):
    print('------调用test1------')


print('开始调用test1')
test1(1)
