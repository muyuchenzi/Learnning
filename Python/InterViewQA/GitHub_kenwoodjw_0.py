import re

class Demo():
    class_var = 0

    def __init__(self, name):
        self.name = name


def list_Demo():
    list_var = ['one', 'two', 'three', 'four']
    dict_var = {
        "one": 1,
        "two": 2,
        "three": 3
    }
    sss = [dict_var.get(i, "not_find") for i in list_var]
    ttt = map(lambda x: dict_var.get(x), list_var)
    for inde in ttt:
        print(inde)
    xx = [x for x in range(1, 100)]
    print(sss, xx)


def string_demo():
    string_var = "djfajfweuriuer0938435987197@#%^$^&%%)(*(&(&%^^%$%^$^*&)&(&fdajfuadojfdurq"
    # string find
    string_var.find('0938435')
    string_var.index("0938435")
    string_var.rfind("0938435")






if __name__ == '__main__':
    myObj = Demo("lizhenxiang")
    hasattr(myObj, "name")
    hasattr(myObj, "age")
    getattr(myObj, "name")
    setattr(myObj, "age", 21)
    getattr(myObj, "age")
