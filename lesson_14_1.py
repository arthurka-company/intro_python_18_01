# public - публичный

# protected - защищенный
# private - приватный




'test'.upper()


class Test:
    def public(self):
        print('public')
        self._protected()

    def _protected(self):
        print('protected')
        self.__private()

    def __private(self):
        print('private')




# obj = Test()
# # obj.public()
# # obj._protected()
# obj._Test__private()
# obj.__private()
