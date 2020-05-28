def parent_func(name):
    def set_func(func):
        def cal_func(*args, **kwargs):
            print('------%s的数据验证------' % name)
            return func(args, kwargs)
        return cal_func
    return set_func


@parent_func('test1')
def test1(para, *args, **kwargs):
    print('------调用test1------')


@parent_func('test2')
def test2(para, *args, **kwargs):
    print('------调用test2------')
    return 'ok...'


test1(1)
print('=' * 30, '我是分割线', '=' * 30)
print(test2('a', 'b', 'c', d=1, e='2'))
