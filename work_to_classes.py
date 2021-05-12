class Dog:
    def __init__(self, name: str, height: int, weight: int, age: int, master, address: str = 'Minsk'):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        """Ограничение доступа"""
        self.__master = master
        self.__address = address

    def bark(self):
        print(f'{self.name} Wolf')

    def jump(self):
        print(f'{self.name} Jump')

    def run(self):
        print(f'{self.name} run')

    def get_master(self):
        return self.__master

    """Определение атрибута mater"""

    def set_master(self, master):
        if len(master) < 5:
            print(f'Wrong small name - {master}')
            pass
        else:
            self.__master = master
    @property
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


"""Инициализация атрибута метода класса происходит здесь"""
dog = Dog(name='Jack', height=50, weight=50, age=1, master='Dima')
print(dog.get_master())
dog.set_master(master='Nastia')
print(dog.get_master())
dog.set_address(address='Cherven')
print(dog.get_address)

