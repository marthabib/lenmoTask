class Singleton():
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Lenmo():
    __metaclass__ = Singleton
    __balance = 0
    __profitAmount = 3

    @property
    def balance(self):
        return self.__balance

    @property
    def profitAmount(self):
        return self.__profitAmount

    @classmethod
    def gain(cls):
        cls.__balance += cls.__profitAmount
