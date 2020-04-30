# sorted
import random


def sorted_func():
    alist = [i for i in range(30)]
    random.shuffle(alist)
    order_list_1 = sorted(alist, key=lambda x: str(x))
    order_list_2 = sorted(alist, key=lambda x: int(x))
    dict_test = {
        "b": 67,
        'a': 23,
        "c": 45,
        "aa": 34
    }
    order_dict = sorted(dict_test.items(), key=lambda x: x[0])
    add_list = [i * 11 for i in range(10, 20)]
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    inter_list = list(set(list1) & set(list2))
    list1.extend(list2)
    unique_list = list(set(list1))
    '''
    python中内置的数据结构
    1、整型int，长整型long，浮点型float，复数complex
    2、字符串str，列表list，元组tuple
    3、字典dict，集合set
    '''


