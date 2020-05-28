class Test:
    """这是类的文档字符串"""
    num = 0

    def __init__(self, a):
        self.a = a

    def cal(b):
        return self.a + b


print('--------------------直接操作类对象--------------------')
print('\n--------Test.__doc__------------')
print(Test.__doc__)
print('\n--------Test.__dict__------------')
print(Test.__dict__)
print('\n--------Test.__mro__------------')
print(Test.__mro__)
print('\n--------Test.操作属性------------')
print(hasattr(Test, 'new_attr'))
setattr(Test, 'new_attr', 'this is new attr')
print(getattr(Test, 'new_attr'))
print('---------------------操作实例对象--------------------')
test = Test(1)
print(test)
print(test.__class__)
print(test.__class__.__class__)
print(test.__class__.__class__.__class__)
print(type(Test))
print(type(test))
print('--------------------使用type创建类,第一个参数为类名,第二个参数为父类名(元组),第三个参数为类属性(字典)--------------------')
print('\n--------创建普通类------------')
NewTest = type('NewTest2', (), {})  # 一般会NewTest和NewTest2会写成同样的名字
print(NewTest)
print(type(NewTest))
newtest = NewTest()
print(newtest)
print(type(newtest))
print('\n--------创建带有属性的类,这些属性为类属性------------')
Test2 = type('Test2', (), {'name': 'python', 'age': 18})
# help(Test2)
a = Test2()
print(a.name)
print(a.age)
b = Test2()
print(b.name)
print(b.age)
print('\n--------创建带有方法的类------------')
print('--1.定义类方法func1--')


@classmethod
def func1(cls):
    print('这是func1')


print('--2.定义实例方法--')


def func2(self):
    print('这是func2')


Test3 = type('Test3', (), {'name': 'xiaoming', 'age': 20, 'func1': func1, 'func2': func2})
# help(Test3)
test3 = Test3()
test3.func1()
test3.func2()
print('\n--------创建继承父类的子类------------')
Test4 = type('Test4', (Test2, Test3), {'core': 100})
# help(Test4)
test4 = Test4()
print('--类的__mro__属性为其继承父类的顺序,即super()对应的父类--')
print(Test4.__mro__)
print('--子类直接使用父类的类属性,这里获取的下一个父类为Test2--')
print(test4.name)
print('\n--------创建带有实例属性的类------------')


def __init__(self, a):
    self.a = a
    print(self.a)


Test5 = type('Test5', (), {'name': 'xiaohua', '__init__': __init__})
test5 = Test5(5)
