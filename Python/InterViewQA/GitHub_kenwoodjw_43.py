class Car(object):
    def __init__(self, name, loss):
        self.name = name
        self.loss = loss

    def get_name(self):
        return self.name

    def get_price(self):
        return self.loss[0]

    def get_loss(self):
        return self.loss[1] * self.loss[2]


if __name__ == '__main__':
    Bmw = Car("宝马", [60, 9, 500])
    print(getattr(Bmw, "name"))
    print(dir(Bmw))
