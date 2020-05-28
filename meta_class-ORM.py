class ModelMetaClass(type):
    """
    这个元类的作用是,将原本Goods类中定义的类属性(字段)删除,并同时用一个新的属性__mapping__去存这些类属性
    将这些字段属性单独抽出来放到字典里面的原因是方便遍历
    """

    def __new__(self, class_name, class_parents, class_attr):
        mappings = dict()
        # 将字段属性抽出放入新字典mapping中
        for name, value in class_attr.items():
            if isinstance(value, tuple):
                mappings[name] = value[0]
        # 删除原属性字典中的字段属性,因为已经用不到了
        for k in mappings.keys():
            class_attr.pop(k)
        # 新增mapping属性指向mapping字典
        class_attr['mappings'] = mappings
        # 将类名作为表名
        class_attr['table'] = class_name

        return type(class_name, class_parents, class_attr)


class Goods(metaclass=ModelMetaClass):
    goods_id = ('goods_id', 'int unsigined')
    name = ('name', 'varchar(20)')
    desc = ('desc', 'varchar(200)')
    # 上面属性经过元类的__new__方法后,转化为
    # mapping = {
    #     'goods_id': ('goods_id', 'int unsigined'),
    #     'name': ('name', 'varchar(20)'),
    #     'desc': ('desc', 'varchar(200)'),
    # }
    # table = Goods

    def __init__(self, **kwargs):
        # 将传入的参数设置成实例属性
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fileds = []  # 数据库字段名
        values = []  # 插入的值
        for name, value in self.mappings.items():
            # 将获取的字段名存入fileds
            fileds.append(value)
            # 将字段名对应的实例属性值存入values
            value = getattr(self, name, None)
            # 如果是字符串类型则前后拼上双引号
            if isinstance(value, str):
                value = '"' + value + '"'
            values.append(value)
        sql = 'insert into %s( %s) values (%s)' % (self.table, ','.join(fileds),
                                                   ','.join([str(value) for value in values]))
        print(sql)


goods = Goods(goods_id=12, name='草莓', desc='这是草莓的简介')
goods.save()
goods2 = Goods(name='香蕉', desc='这是香蕉的简介', goods_id=13)
goods2.save()
