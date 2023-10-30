#инкапсуляция

class Bank:
    def __init__(self, name, money, password):
        self.name = name
        self._money = money
        self.__passw = password

    def printn(self):
        print(self.name, self._money)

    def sawe(self):
        print(self.__passw)


b = Bank('beka', 0, '234ewsdt543ewdf')
b.sawe()
b.printn()
b._money = 100000000000
b.__passw = 0
# print(f'{b.__passw}')
# print(b.__passw)
print(dir(b))
b.printn()
b.sawe()


from art import tprint
import  colorama
print(colorama.Back.BLACK)
print(colorama.Fore.RED)
tprint('clok')


