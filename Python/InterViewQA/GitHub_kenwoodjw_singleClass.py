def singleon(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleon
class Foo(object):
    pass


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls2(object):
    def __int__(self):
        pass


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    cls21 = Cls2()
    cls22 = Cls2()
