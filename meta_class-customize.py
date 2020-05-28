class UpperAttrMetaClass(type):
    def __new__(cls, class_name, class_parents, class_attr):
    	"""__new__方法时在__init__之前被调用的特殊方法,是python中真正的构造方法(不是__init__)
    	其作用是创建一个对象并返回该对象,而__init__的作用只是初始化对象的属性
    	在实现单例模式时可以用到这个__new__方法
    	这里因为我们需要通过该方法将一个传入的类对象改造一下并返回一个新的类对象,因此使用__new__方法
    	除了第一个固定参数cls外,其他自定义的参数分别为传入的类名,传入类的父类,传入类的属性
    	"""
    	# 定义一个空字典,用来存放新的类属性
        new_attr = dict()
        # 循环遍历原来的类属性,并将非__开头的属性的属性名改成大写,并存入新的字典
        for name, value in class_attr.items():
            if not name.startswith('__'):
                new_attr[name.upper()] = value
            else:
                new_attr[name] = value
        # 使用type创建一个新的类对象,该类对象的属性使用上面新字典中的属性
        return type(class_name, class_parents, new_attr)


class Test(object, metaclass=UpperAttrMetaClass):
    name = 'python'

# 类Test在语句创建中,属性name为小写,但是语句创建后,属性变成了大写NAME
print('Test是否有name属性', hasattr(Test, 'name'))
print('Test是否有NAME属性', hasattr(Test, 'NAME'))

# 运行结果为:
# Test是否有name属性 False
# Test是否有NAME属性 True
