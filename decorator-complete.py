# 装饰器为了满足被装饰函数的所有参数和返回值
# 1.需要在cal_func中写上不定长参数*args和**kwargs
#   1.1 注意使用的参数名就叫做args和kwargs,而不是*args和**kwargs
#       这里参数中写的*和**是为了让python解释器将多余的参数分为元组tuple和字典dic
#   1.2 而下面调用func传入的参数时,也加上了*和**,这里*和**的作用是将args和kwargs拆包
#       使传入的参数拆成在同一个维度上面,相当于拆成func('a', 'b', 'c', d=1, e='2')
#       如果调用func传入时参数不带*,则相当于传入的参数为func(('a', 'b', 'c'), {'d': 1, 'e': '2'})
#       这样会导致解释器解析func的参数时,认为传入的是两个值,一个是元组,一个是字典
#       然后在func中处理参数时,将第一个元组通过para接收,第二个字典通过*args接收,导致最终结果与预期不一样
# 2.在cal_func中调用传入的func前,添加return,这样如果被装饰函数也有return的话,可以将最终的结果也return出来

def set_func(func):
    def cal_func(*args, **kwargs):
        print('------数据验证------')
        print('args', args)
        print('kwargs', kwargs)
        return func(args, kwargs)
    return cal_func


@set_func
def test1(para, *args, **kwargs):
    print('------调用test1------')
    print('------para------', para)
    print('------*args------', args)
    print('------*kwargs------', kwargs)


@set_func
def test2(para, *args, **kwargs):
    print('------调用test2------')
    print('------para------', para)
    print('------*args------', args)
    print('------*kwargs------', kwargs)
    return 'ok...'


test1(1)
print('=' * 30, '我是分割线', '=' * 30)

test1('a')
print('=' * 30, '我是分割线', '=' * 30)

test1('a', 'b', 'c')
print('=' * 30, '我是分割线', '=' * 30)

test1('a', 'b', 'c', d=1, e='2')
print('=' * 30, '我是分割线', '=' * 30)

print(test2('a', 'b', 'c', d=1, e='2'))
