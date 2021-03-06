# 2、原类别进行处理
# 这里先理解下函数参数里面的self和cls.这个self和cls是对类或者实例的绑定,对于一般的函数来说我们可以这么调用foo(x),
# python中的方法总共有四类，一个是最常见的方法，一个是实例方法一个是类方法一个是静态方法
# 实例对于实例方法、静态方法、类方法都能进行调用
# 对象能对静态方法、类方法进行调用
# 静态方法必须绑定对象或者实例，类似于JavaScript必须要绑定this值
# 类变量是对象共享的数据，实例对象可以对类变量进行处理，但是改的是自己本身的数据,如果需要该类的变量直接使用类进行引用
# 然后就能进行修改了 注意这边的数据必须是值类型，如果是引用类型的数据那么就会导致实例对象可以修改类对象的方法
def foo(x):
    print(f"executing normal funcition {x}")


class A(object):
    class_var = 0

    def __init__(self, name):
        self.name = name
        A.class_var += 1

    def foo(self, x):
        print(f"executing object funciton {self},{x}")

    @classmethod
    def class_foo(cls, x):
        print(f"executing  class_foo({cls},{x})")

    @staticmethod
    def static_foo(x):
        print(f"executing static_foo {x}")


if __name__ == '__main__':
    '''四种不同方法-demo'''
    foo(1)
    objA = A("chenzi")
    objA.foo(2)
    objA.class_foo(3)
    objA.static_foo(4)
    A.class_foo(5)
    A.static_foo(6)
    objA1 = A("chenzi01")
    objA1.class_var = 'objA1'
    print(objA1.class_var)
    print(objA1.name)
    A.class_var='classValue'
    objA2 = A("chenzi02")
    print(objA2.class_var)
    print(objA2.name)
    objA3 = A("chenzi03")
    print(objA3.class_var)
    print(objA3.name)
