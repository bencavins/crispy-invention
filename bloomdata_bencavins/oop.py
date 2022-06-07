# Object Oriented Programming (OOP)
# class == blueprint, how to build an object
# object == instance of build object
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def calc_distance(self, other_point):
        self.x - other_point.x


p1 = Point(1, 3)
p2 = Point(6, 3.14)


class Product:
    def __init__(self, price, weight, name):
        self.price = price
        self.weight = weight
        self.name = name


class Computer(Product):
    def __init__(self, price, weight, name, cpu, os):
        self.cpu = cpu
        self.os = os
        super().__init__(price, weight, name)


p1 = Product(5.0, 3, 'coffee')
p2 = Computer(100, 10, 'macbook', 'inteli8', 'macosx')
print(p2.price, p2.name, p2.weight)





def report(products):
    total_price = 0
    for product in products:
        total_price += product.price
    
    avg_price = total_price / len(products)


class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


class Dog(Animal):    
    def bark(self):
        print(self.name + ' says: bark!')


class BigDog(Dog):
    def bark(self):
        print(self.name + ' says: BARK!!!')


class LittleDog(Dog):
    pass


class Cat(Animal):
    def meow(self):
        print('meow!')


# my_dog = Dog('fido')
# dog2 = Dog('rex', 3)

# print(my_dog.name, dog2.name)
# print(my_dog.age, dog2.age)
# my_dog.bark()
# dog2.bark()