# class 进行创建对象的时候一般是首先是创建一个类、实例化一个对象、实例对象的初始化
# 分别执行__metaclass__,__new__,__init__
# 对象的拷贝 引用类型的数据进行赋值的时候传递的是个引用，
#
import copy

a = [1, 2, 3, 4, ['a', 'b']]

b = a
o = a.copy()
c = copy.copy(a)
d = copy.deepcopy(a)
a[0] = "modify"
a[4][0] = "m"
a.append("test")
print(b)
print(o)
print(c)
print(d)

l1 = l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = list({}.fromkeys(l1))
items = [('name', 'earth'), ('port', '80')]
dict2 = dict(items)

key_list = ["one", 'two', "three"]
val_list = [1, 2, 3]
dic_res = dict(zip(key_list, val_list))
