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
