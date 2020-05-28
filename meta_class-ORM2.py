class Goods(object):
    goods_id = ('goods_id', 'int unsigined')
    name = ('name', 'varchar(20)')
    desc = ('desc', 'varchar(200)')

    def __init__(self, **kwargs):
        # 获取表名,即对应类的名字
        self.table = self.__class__.__name__
        # 将传入的参数设置成实例属性
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fileds = []
        values = []
        # 循环类属性
        for name, value in self.__class__.__dict__.items():
            # 如果类属性的值为元组,则认为其为定义的字段属性
            if isinstance(value, tuple):
                # 将获取的字段名存入fileds
                fileds.append(value[0])
                # 将字段名对应的实例属性值存入values
                value = getattr(self, name, None)
                # 如果是字符串类型则前后拼上双引号
                if isinstance(value, str):
                    value = '"' + value + '"'
                values.append(value)

        sql = 'insert into % s(% s) values (%s)' % (self.table, ','.join(fileds),
                                                    ','.join([str(value) for value in values]))
        print(sql)


goods = Goods(goods_id=12, name='草莓', desc='这是草莓的简介')
goods.save()
goods2 = Goods(name='香蕉', desc='这是香蕉的简介', goods_id=13)
goods2.save()
