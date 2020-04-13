# python 数据自省
# python 的参数一般是有三个方式，
# 第一个就是a,b,c,调用使用（1,2,3）这样就会一一对应
# 第二个就是a,b,c,调用的时候是使用*args 调用（1,2,3）会直接args是一个输入参数的tuple
# 第三个是使用a=1,b=2,c=3,这样**kwargs 这样kwargs={"a":1,"b":2,"c":3}
# 如果函数调用使用list 调用的话，函数调用可以使用*进行结构，JavaScript中使用的是...。
def print_everyThing(**kwargs):
    for name, value in kwargs.items():
        print(f"{name},{value} in {kwargs}")


print_everyThing(a="one", b="two")


def print_list_arg(*args):
    print(args, type(args))


def print_three_things(a, b, c):
    print(f"{c}->{b}->{a}")


print_three_things(1, 2, 3)
print_list_arg(1, 2, 3)
