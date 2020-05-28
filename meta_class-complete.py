class Parent:
    parent_name = 'parent'


class Son1(Parent):
    son_name = 'xiaoming'

    def __init__(self, a):
        self.a = a

    def add(self, b):
        return self.a + b

    @classmethod
    def print_class(cls):
        print('调用了类方法')

    @staticmethod
    def print_static():
        print('调用了静态方法')


son1 = Son1(100)
print('-------------------实例对象son1的操作----------------------')
print('parent_name 属性:', son1.parent_name)
print('son_name 属性:', son1.son_name)
print('调用了实例方法add:', son1.add(10))
son1.print_class()
son1.print_static()

# 初始化方法
def __init__(self, a):
    self.a = a


# 实例方法
def add(self, b):
    return self.a + b


# 类方法
@classmethod
def print_class(cls):
    print('调用了类方法')


# 静态方法
@staticmethod
def print_static():
    print('调用了静态方法')


Son = type('Son', (Parent,), {'son_name': 'xiaoming',
                              '__init__': __init__,
                              'add': add,
                              'print_class': print_class,
                              'print_static': print_static})

son = Son(100)
print('-------------------实例对象son的操作----------------------')
print('parent_name 属性:', son.parent_name)
print('son_name 属性:', son.son_name)
print('调用了实例方法add:', son.add(10))
son.print_class()
son.print_static()
