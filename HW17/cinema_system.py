# Выбрать систему, которая может быть описана несколькими классами.
#
# Описать исползуя классы и применить принципы ООП:
# - Наследование
# - Абстрактные классы и/или интерфейсы
# - Сокрытие
# - Инкапсуляция
#
# У классов должно быть состояние (поля) и реализация поведения через методы.
# Требований к типам полей (экземпляра/класса) и методов (экземпляра/класса/статические) нет, по необходимости как вы видите.
# Написать код который создает необходимые экземпляры и демонстрирует работу систему.
# Ограничений на количество классов нет, но конечно их тут будет не пара.
# Это задание на это и следующие занятие. Пока советую выбрать систему, и порисовать из чего она состоит.
from abc import ABCMeta, abstractmethod, ABC


class Person:
    user_counter = 0

    def __init__(self, first_name, last_name, date_of_birth, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.email = email
        Person.user_counter += 1

    def get_info(self):
        print(f'{self.first_name}, {self.last_name}, {self.date_of_birth}, {self.phone}, {self.email}')


class Client(Person):
    client_counter = 0

    def __init__(self, first_name, last_name, date_of_birth, phone, email, ticket):
        super().__init__(first_name, last_name, date_of_birth, phone, email)
        self.ticket = ticket
        Client.client_counter += 1

    def get_info(self):
        print(f'{self.first_name}, {self.last_name}, {self.date_of_birth}, {self.phone}, {self.email}, {self.ticket}')


class Staff(Person):
    staff_counter = 0

    def __init__(self, first_name, last_name, date_of_birth, phone, email, department, id, salary):
        super().__init__(first_name, last_name, date_of_birth, phone, email)
        self.department = department
        self.id = id
        self.__salary = salary
        Staff.staff_counter += 1

    def get_info(self):
        print(
            f'{self.first_name}, {self.last_name}, {self.date_of_birth}, {self.phone}, {self.email}, {self.department}, {self.id}')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @salary.deleter
    def salary(self):
        del self.__salary


class Purchase(metaclass=ABCMeta):

    @abstractmethod
    def buy(self):
        pass


class Ticket(Purchase, ABC):
    def buy(self):
        return 'Ticket is bought'


class Food(Purchase, ABC):
    def buy(self):
        return 'Cola and pop corn are bought'


class GeneralFlow:
    person1 = Person("Alex", "Kud", "10-10-1990", "+38095361147", "test@gmail.com")
    person1.get_info()

    client1 = Client("John", "Dou", "10-10-1984", "+38095361347", "test1@gmail.com", "00001")
    client1.get_info()

    staff1 = Staff("Sam", "Smith", "01-12-2001", "+38095317743", "test3@gmail.com", "Marketing", "23123123", "3200")
    staff1.get_info()
    print(staff1.salary)
    staff1.salary = 7000
    print(staff1.salary)

    ticket = Ticket().buy()
    food = Food().buy()
