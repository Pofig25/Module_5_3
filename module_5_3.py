class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors =  number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self):
        return (self.number_of_floors)

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):                                                    # __eq__
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):                                                   # __add__
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):                                                  # __iadd__
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):                                                  # __radd__
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __gt__(self, other):                                                    # __gt__
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):                                                    # __ge__
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):                                                    # __lt__
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):                                                    # __le__
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):                                                    # __ne__
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# h1.go_to(5)
# h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
# print(len(h1))
# print(len(h2))

print(h1==h2)               # __eq__

h1 = h1 + 10                # __add__
print(h1)
print(h1 == h2)

h1 += 10                    # __iadd__
print(h1)

h2 = 10 + h2                # __radd__
print(h2)

print(h1 > h2)              # __gt__
print(h1 >= h2)             # __ge__
print(h1 < h2)              # __lt__
print(h1 <= h2)             # __le__
print(h1 != h2)             # __ne__


'''
Необходимо дополнить класс House следующими специальными методами:

__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.

Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:

isinstance(other, int) - other указывает на объект типа int.

isinstance(other, House) - other указывает на объект типа House.

Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
'''