# 类似于JavaScript的对象解构，字典也可以进行{**dict}进行解构深拷贝
# 类似于JavaScript的array，list 也可以进行[*list]进行解构深拷贝

import os
import random
import math


def print_directory_contents(sPath):
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)


def random_list(list):
    list_var = [i for i in range(20)]
    list_temp = list_var
    list_test = [*list_var, "two"]
    list_var[0] = "one"
    print(list_temp)
    print(list_test)
    random.shuffle(list_var)


def order_dict(dict):
    d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
    test = d
    temp = {**d}
    d['a'] = 3
    print(test)
    print(temp)
    # 1、sorted对key 进行排序
    sorted(d.items(), key=lambda x: x[1])
    # 2、使用 字典推导式
    key_order = sorted(d)
    result = {key_ord: d[key_ord] for key_ord in key_order}
    return result


def del_list_same_item():
    random_list_var_1 = []
    for i in range(40):
        random_list_var_1.append(random.randrange(1, 30))
    unique_list_var_1 = list(set(random_list_var_1))
    random_list_var_2 = []
    for i in range(20):
        random_list_var_2.append(random.randrange(15, 30))
    unique_list_var_2 = list(set(random_list_var_2))
    union_result = list(set(unique_list_var_1) & set(unique_list_var_2))
    excep_result = list(set(unique_list_var_1) ^ set(unique_list_var_2))
    or_result = list(set(unique_list_var_1) | set(unique_list_var_2))


if __name__ == '__main__':
    print_directory_contents(sPath='GitHub_kenwoodjw_yeild.py')
